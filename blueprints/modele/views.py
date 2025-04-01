from flask import Blueprint, request, jsonify
from service.modele_service import ModeleService
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools


class ModeleViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.sql_injection_tools = SQLInjectionTools()
        self.modele_service = ModeleService()
        self.modele_bp = Blueprint('modele', __name__, template_folder='templates')
        self.modele_routes()

    def modele_routes(self):
        @self.modele_bp.route('/add-modele', methods=['POST'])
        def add_modele():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom_modele')
                marque = data.get('id_marque')
                if self.sql_injection_tools.detect_sql_injection([nom, marque]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.modele_service.add_modele(nom, marque)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.modele_bp.route('/update-modele', methods=['PUT'])
        def update_modele():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_modele = data.get('id_modele')
                nom = data.get('nom_modele')
                marque = data.get('id_marque')
                if self.sql_injection_tools.detect_sql_injection([id_modele, nom, marque]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.modele_service.update_modele(id_modele, nom, marque)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.modele_bp.route('/delete-modele/<int:id_modele>', methods=['DELETE'])
        def delete_modele(id_modele):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_modele]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.modele_service.delete_modele(id_modele)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.modele_bp.route('/get-modeles', methods=['GET'])
        def get_modeles():
            if self.user_tools.check_user_in_session('admin'):
                status, modeles = self.modele_service.find_all_modele()
                return jsonify({'status': 'success', 'modeles': modeles})
            return {'status': 'failed'}


if __name__ == '__main__':
    pass
