from flask import Blueprint, request, jsonify
from service.magasin_service import MagasinService
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools


class MagasinViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.sql_injection_tools = SQLInjectionTools()
        self.magasin_service = MagasinService()
        self.magasin_bp = Blueprint('magasin', __name__, template_folder='templates')
        self.magasin_routes()

    def magasin_routes(self):
        @self.magasin_bp.route('/add-magasin', methods=['POST'])
        def add_magasin():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom_magasin')
                id_salle = data.get('id_salle')
                if self.sql_injection_tools.detect_sql_injection([nom, id_salle]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.magasin_service.add_magasin(nom, id_salle)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'error', 'message': 'Erreur Serveur'}

        @self.magasin_bp.route('/update-magasin/<int:id_magasin>', methods=['PUT'])
        def update_magasin(id_magasin):
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom_magasin')
                id_salle = data.get('id_salle')
                if self.sql_injection_tools.detect_sql_injection([nom, id_salle]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.magasin_service.update_magasin(id_magasin, id_salle, nom)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'error', 'message': 'Erreur Serveur'}

        @self.magasin_bp.route('/delete-magasin/<int:id_magasin>', methods=['DELETE'])
        def delete_magasin(id_magasin):
            if self.user_tools.check_user_in_session('admin'):
                if self.sql_injection_tools.detect_sql_injection([id_magasin]):
                    return {'status': 'error', 'message': 'Problème de sécurité détecté'}
                status = self.magasin_service.delete_magasin(id_magasin)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'error', 'message': 'Erreur Serveur'}

        @self.magasin_bp.route('/get-magasins', methods=['GET'])
        def get_magasins():
            if self.user_tools.check_user_in_session('admin'):
                status, magasins = self.magasin_service.find_all_magasin()
                return jsonify({'status': 'success', 'magasins': magasins})
            return {'status': 'error', 'message': 'Erreur Serveur'}

        @self.magasin_bp.route('/get-magasin', methods=['GET'])
        def get_magasin():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_magasin = data.get('id_magasin')
                status, magasin = self.magasin_service.find_magasin_by_id(id_magasin)
                return jsonify({'status': 'success', 'magasin': magasin})
            return {'status': 'error', 'message': 'Erreur Serveur'}


if __name__ == '__main__':
    pass
