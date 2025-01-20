from flask import Blueprint, request, jsonify, url_for, redirect

from service.utilisateur_service import UtilisateurService
from tools.user_tools import UserTools


class ClientViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.client_service = UtilisateurService()
        self.client_bp = Blueprint('client', __name__, template_folder='templates')
        self.client_routes()

    def client_routes(self):
        @self.client_bp.route('/location', methods=['GET'])
        def location_client():
            if self.user_tools.check_user_in_session('user'):
                return 'Welcome to the client home page'
            return redirect(url_for('auth.login'))
