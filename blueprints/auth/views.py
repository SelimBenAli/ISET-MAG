from flask import Blueprint, render_template, request, session, flash, url_for, redirect

from service.utilisateur_service import UtilisateurService
from tools.cryption_tools import CryptionTools
from tools.user_tools import UserTools


class AuthViews:
    def __init__(self):
        self.user_tools = UserTools()
        self.utilisateur_service = UtilisateurService()
        self.cryption_tools = CryptionTools()
        self.admin_bp = Blueprint('auth', __name__, template_folder='templates')
        self.auth_routes()

    def auth_routes(self):
        @self.admin_bp.route('/login', methods=['GET'])
        def login():
            if self.user_tools.check_user_in_session('user'):
                return redirect(url_for('client.location_client'))
            return render_template('client/login.html')

        @self.admin_bp.route('/client-login-request', methods=['POST'])
        def login_post():
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            status, user = self.utilisateur_service.find_utilisateur_by_mail(email)
            print("user", user)
            if status == 'success':
                if user[0]['mdp_utilisateur'] != self.cryption_tools.crypt_sha256(password):
                    return {'status': 'failed', 'message': 'Utilisateur Non Trouvé'}
                my_user = user[0].pop('mdp_utilisateur')
                session['user'] = my_user
                return {'status': 'success', 'user': my_user}
            elif status == 'failed':
                return {'status': 'failed', 'message': 'Utilisateur Non Trouvé'}
            else:
                flash('Erreur Serveur', 'error')
                return {'status': 'error'}

        @self.admin_bp.route('/logout', methods=['GET'])
        def logout():
            session['user'] = None
            return redirect(url_for('auth.login'))

