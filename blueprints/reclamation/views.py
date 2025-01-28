from flask import Blueprint, jsonify
from service.reclamation_service import ReclamationService
from tools.user_tools import UserTools


class ReclamationViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.reclamation_service = ReclamationService()
        self.reclamation_bp = Blueprint('reclamation', __name__, template_folder='templates')
        self.reclamation_routes()

    def reclamation_routes(self):
        @self.reclamation_bp.route('/delete-reclamation/<int:id_reclamation>', methods=['DELETE'])
        def delete_reclamation(id_reclamation):
            if self.user_tools.check_user_in_session('admin'):
                status = self.reclamation_service.delete_reclamation(id_reclamation)
                if status != 'failed':
                    return {'status': 'success'}
            return {'status': 'failed'}

        @self.reclamation_bp.route('/get-reclamations', methods=['GET'])
        def get_reclamations():
            if self.user_tools.check_user_in_session('admin'):
                status, reclamations = self.reclamation_service.find_all_reclamation()
                print(reclamations)
                return jsonify({'status': 'success', 'reclamations': reclamations})
            return {'status': 'failed'}
