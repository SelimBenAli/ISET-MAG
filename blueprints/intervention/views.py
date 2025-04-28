from flask import Blueprint, request, jsonify, session

from service.hardware_service import HardwareService
from service.intervention_service import InterventionService
from service.utilisateur_service import UtilisateurService
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools


class InterventionViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.sql_injection_tools = SQLInjectionTools()
        self.intervention_service = InterventionService()
        self.utilisateur_service = UtilisateurService()
        self.hardware_service = HardwareService()
        self.intervention_bp = Blueprint('intervention', __name__, template_folder='templates')
        self.intervention_routes()

    def intervention_routes(self):
        @self.intervention_bp.route('/add-intervention', methods=['POST'])
        def add_intervention():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                code_user = data.get('user')
                code_hardware = data.get('hardware')
                if self.sql_injection_tools.detect_sql_injection([code_user, code_hardware]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                # date_debut = data.get('date_debut')
                # id_salle = data.get('id_salle')
                # if id_salle is None or id_salle == '' or id_salle == 0 or id_salle == '0':
                #     id_salle = ' NULL '
                status, u = self.utilisateur_service.find_utilisateur_by_code_barre(code_user)
                status, h = self.hardware_service.find_hardware_by_code(code_hardware)
                print(u, h)
                if u is not None and h is not None:
                    id_user = u[0]['id_utilisateur']
                    id_hardware = h[0]['id_hardware']
                else:
                    return {'status': 'failed'}

                status, i = self.intervention_service.find_intervention_by_used_hardware(id_hardware)

                if len(i) > 0:
                    return {'status': 'failed', 'message': 'Hardware déjà pris en intervention'}
                id_admin = session['admin']['id_admin']
                status = self.intervention_service.add_intervention(id_user, None, ' NULL ', None,
                                                                    id_hardware, id_admin)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed', 'message': 'Erreur de session'}

        @self.intervention_bp.route('/update-intervention/<int:id_intervention>', methods=['PUT'])
        def update_intervention(id_intervention):
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_user = data.get('id_user')
                date_debut = data.get('date_debut')
                id_salle = data.get('id_salle')
                if id_salle is None or id_salle == '' or id_salle == 0 or id_salle == '0':
                    id_salle = ' NULL '
                id_hardware = data.get('id_hardware')
                if self.sql_injection_tools.detect_sql_injection([id_intervention, id_user, date_debut, id_salle, id_hardware]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.intervention_service.update_intervention(id_intervention, id_user, date_debut,
                                                                       id_salle,
                                                                       id_hardware)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.intervention_bp.route('/delete-intervention/<int:id_intervention>', methods=['DELETE'])
        def delete_intervention(id_intervention):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_intervention]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.intervention_service.delete_intervention(id_intervention)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions', methods=['GET'])
        def get_interventions():
            if self.user_tools.check_user_in_session('admin'):
                status, interventions = self.intervention_service.find_all_intervention()

                return jsonify({'status': 'success', 'interventions': interventions})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-user-code/<string:code>', methods=['GET'])
        def get_interventions_uc(code):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([code]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status, user = self.utilisateur_service.find_utilisateur_by_code(code)
                status, interventions = self.intervention_service.find_intervention_by_user(user[0]['id_utilisateur'])

                return jsonify({'status': 'success', 'interventions': interventions})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-hard-code/<string:code>', methods=['GET'])
        def get_interventions_hc(code):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([code]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status, hard = self.hardware_service.find_hardware_by_code(code)
                status, interventions = self.intervention_service.find_intervention_by_hardware(hard[0]['id_hardware'])

                return jsonify({'status': 'success', 'interventions': interventions})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-hard-num/<string:code>', methods=['GET'])
        def get_interventions_hn(code):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([code]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status, hard = self.hardware_service.find_hardware_by_numero_inventaire(code)
                status, interventions = self.intervention_service.find_intervention_by_hardware(hard[0]['id_hardware'])

                return jsonify({'status': 'success', 'interventions': interventions})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-closed/<int:page>', methods=['GET'])
        def get_interventions_closed(page):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([page]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                number = 10
                begin = (page - 1) * number
                status, pages = self.intervention_service.find_number_closed_interventions()
                status, interventions = self.intervention_service.find_closed_intervention_with_limit(begin, number)
                if status == 'success':
                    if pages % number != 0:
                        page_number = pages // number + 1
                    else:
                        page_number = pages // number

                    return jsonify(
                        {'status': 'success', 'interventions': interventions, 'pages': page_number,
                         'current_page': page,
                         'nombre_totale': pages})
            return {'status': 'failed'}

        @self.intervention_bp.route('/get-interventions-current/<int:page>', methods=['GET'])
        def get_interventions_current(page):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([page]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                number = 10
                begin = (page - 1) * number
                status, pages = self.intervention_service.find_number_current_interventions()
                status, interventions = self.intervention_service.find_current_intervention_with_limit(begin, number)
                if status == 'success':
                    if pages % number != 0:
                        page_number = pages // number + 1
                    else:
                        page_number = pages // number

                    return jsonify(
                        {'status': 'success', 'interventions': interventions, 'pages': page_number,
                         'current_page': page,
                         'nombre_totale': pages})
            return {'status': 'failed'}

        @self.intervention_bp.route(
            '/get-interventions-limit/<int:page>/<string:status>/<string:code_hard>/<string:code_user>/<string:num_hard>',
            methods=['GET'])
        def get_interventions_limit(page, status, code_hard, code_user, num_hard):
            if self.user_tools.check_user_in_session('admin'):


                if self.sql_injection_tools.detect_sql_injection([page, status, code_hard, code_user, num_hard]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}

                code_hard = code_hard.replace('code_hard_', '')
                code_user = code_user.replace('code_user_', '')
                num_hard = num_hard.replace('num_hard_', '')
                status = status.replace('status_', '')
                ch = ''
                if status == '1':
                    ch += ' AND DateFin IS NULL '
                elif status == '2':
                    ch += ' AND DateFin IS NOT NULL '
                if code_hard != '':
                    status, hard = self.hardware_service.find_hardware_by_code(code_hard)
                    if status == 'success' and len(hard) > 0:
                        hard = hard[0]['id_hardware']
                        ch += f' AND IDHardware = {hard} '
                if code_user != '':
                    status, user = self.utilisateur_service.find_utilisateur_by_code(code_user)
                    if status == 'success' and len(user) > 0:
                        user = user[0]['id_utilisateur']
                        ch += f' AND IDUtilisateur = {user} '
                if num_hard != '':
                    status, hard = self.hardware_service.find_hardware_by_numero_inventaire(num_hard)
                    if status == 'success' and len(hard) > 0:
                        hard = hard[0]['id_hardware']
                        ch += f' AND IDHardware = {hard} '

                number = 10
                begin = (page - 1) * number

                status, pages = self.intervention_service.find_number_interventions(ch)

                status, interventions = self.intervention_service.find_all_intervention_with_limit(ch, begin, number)

                if status == 'success':
                    if pages % number != 0:
                        page_number = pages // number + 1
                    else:
                        page_number = pages // number

                    return jsonify(
                        {'status': 'success', 'interventions': interventions, 'pages': page_number,
                         'current_page': page,
                         'nombre_totale': pages})
            return {'status': 'failed'}

        @self.intervention_bp.route('/close-intervention/<int:id_intervention>', methods=['PUT'])
        def close_intervention(id_intervention):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_intervention]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status, i = self.intervention_service.find_intervention_by_id(id_intervention)

                if len(i) == 0:
                    return {'status': 'failed', 'message': 'Pret introuvable'}
                if i[0]['date_fin_intervention'] is not None:
                    return {'status': 'failed', 'message': 'Intervention déjà fermée'}
                admin = session['admin']['id_admin']
                status = self.intervention_service.close_intervention(id_intervention, admin)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed', 'message': 'Erreur de session'}


if __name__ == '__main__':
    pass
