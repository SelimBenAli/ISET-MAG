from flask import Blueprint, request, jsonify
from service.marque_service import MarqueService
from tools.user_tools import UserTools


class MarqueViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.marque_service = MarqueService()
        self.marque_bp = Blueprint('marque', __name__, template_folder='templates')
        self.marque_routes()

    def marque_routes(self):
        @self.marque_bp.route('/add-marque', methods=['POST'])
        def add_marque():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom_marque')
                status = self.marque_service.add_marque(nom)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.marque_bp.route('/update-marque', methods=['PUT'])
        def update_marque():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_marque = data.get('id_marque')
                nom = data.get('nom_marque')
                status = self.marque_service.update_marque(id_marque, nom)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.marque_bp.route('/delete-marque', methods=['DELETE'])
        def delete_marque():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_marque = data.get('id_marque')
                status = self.marque_service.delete_marque(id_marque)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.marque_bp.route('/get-marques', methods=['GET'])
        def get_marques():
            if self.user_tools.check_user_in_session('admin'):
                status, marques = self.marque_service.find_all_marque()
                return jsonify({'status': 'success', 'marques': marques})
            return {'status': 'failed'}

        @self.marque_bp.route('/get-marque', methods=['GET'])
        def get_marque():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_marque = data.get('id_marque')
                status, marque = self.marque_service.find_marque_by_id(id_marque)
                return jsonify({'status': 'success', 'marque': marque})
            return {'status': 'failed'}
