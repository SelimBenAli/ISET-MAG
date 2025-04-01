from flask import Blueprint, jsonify

from service.hardware_service import HardwareService
from service.reclamation_service import ReclamationService
from service.utilisateur_service import UtilisateurService
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools


class ReclamationViews:
    def __init__(self):
        self.hardware_service = HardwareService()
        self.utitlisateur_service = UtilisateurService()
        self.user_tools = UserTools()
        self.sql_injection_tools = SQLInjectionTools()
        self.reclamation_service = ReclamationService()
        self.reclamation_bp = Blueprint('reclamation', __name__, template_folder='templates')
        self.reclamation_routes()

    def reclamation_routes(self):
        @self.reclamation_bp.route('/delete-reclamation/<int:id_reclamation>', methods=['DELETE'])
        def delete_reclamation(id_reclamation):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_reclamation]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.reclamation_service.delete_reclamation(id_reclamation)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.reclamation_bp.route('/get-reclamations', methods=['GET'])
        def get_reclamations():
            if self.user_tools.check_user_in_session('admin'):
                status, reclamations = self.reclamation_service.find_all_reclamation()

                return jsonify({'status': 'success', 'reclamations': reclamations})
            return {'status': 'failed'}

        @self.reclamation_bp.route('/get-reclamations-limit/<int:page>/<int:status>/<string:user>/<string:inv>', methods=['GET'])
        def get_reclamations_limit(page, status, user, inv):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([page, status, user, inv]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}

                number = 10
                begin = (page - 1) * number
                ch = ''
                if status == 1:
                    ch += ' AND IDTechnicien IS NULL '
                elif status == 2:
                    ch += ' AND IDTechnicien IS NOT NULL '
                user = user.replace('user_', '')
                inv = inv.replace('inv_', '')
                if user != '':
                    status, user = self.utitlisateur_service.find_utilisateur_by_nom_prenom(user)
                    if status == 'success' and len(user) > 0:
                        user = user[0]['id_utilisateur']
                        ch += f' AND IDUtilisateur = {user} '
                if inv != '':
                    status, hardware = self.hardware_service.find_hardware_by_numero_inventaire(inv)
                    if status == 'success' and len(hardware) > 0:
                        hardware = hardware[0]['id_hardware']
                        ch += f' AND IDHardware = {hardware} '
                status, pages = self.reclamation_service.find_reclamation_number(ch)
                status, reclamations = self.reclamation_service.find_all_reclamation_with_limit(ch, number, begin)

                if status == 'success':
                    if pages % number != 0:
                        page_number = pages // number + 1
                    else:
                        page_number = pages // number

                    return jsonify(
                        {'status': 'success', 'reclamations': reclamations, 'pages': page_number, 'current_page': page,
                         'nombre_totale': pages})
            return {'status': 'failed'}


if __name__ == '__main__':
    pass
