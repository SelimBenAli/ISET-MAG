from flask import Blueprint, jsonify, request, session

from service.hardware_service import HardwareService
from service.reclamation_service import ReclamationService
from service.utilisateur_service import UtilisateurService
from tools.user_tools import UserTools


class UserViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.user_service = UtilisateurService()
        self.reclamation_service = ReclamationService()
        self.hardware_service = HardwareService()
        self.user_bp = Blueprint('user', __name__, template_folder='templates')
        self.user_routes()

    def user_routes(self):
        @self.user_bp.route('/add-reclamation', methods=['POST'])
        def add_reclamation():
            if self.user_tools.check_user_in_session('user'):
                data = request.get_json()
                description = data.get('description')
                user = session['user']
                hardware = session['hardware_reclamation']
                description = description.replace('"', "'")
                status = self.reclamation_service.add_reclamation(hardware['id_hardware'],
                                                                  user['id_utilisateur'], 'NULL',
                                                                  description)
                if status == 'success':
                    return jsonify({'status': 'success'})
                return jsonify({'status': 'failed'})
            return jsonify({'status': 'failed'})
