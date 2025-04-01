from flask import Blueprint, render_template, request, session, flash, url_for, redirect

from service.utilisateur_service import UtilisateurService
from tools.cryption_tools import CryptionTools
from tools.sql_injection_tools import SQLInjectionTools
from tools.user_tools import UserTools


class AuthViews:
    def __init__(self):
        self.user_tools = UserTools('dashboard')
        self.utilisateur_service = UtilisateurService()
        self.cryption_tools = CryptionTools()
        self.sql_injection_tools = SQLInjectionTools()
        self.auth_bp = Blueprint('auth', __name__, template_folder='templates')
        self.auth_routes()

    def auth_routes(self):
        @self.auth_bp.route('/login', methods=['GET'])
        def login():
            if self.user_tools.check_user_in_session('user'):
                return redirect(url_for('client.location_client'))
            return render_template('client/login.html')

        @self.auth_bp.route('/client-login-request', methods=['POST'])
        def login_post():
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            if self.sql_injection_tools.detect_sql_injection([email, password]):
                return {'status': 'error', 'message': 'Problème de sécurité détecté'}
            status, user = self.utilisateur_service.find_utilisateur_by_mail(email)
            if status == 'success' and user is not None and user != []:
                if (user[0]['compte_utilisateur'] == 'Active'
                        and user[0]['mdp_utilisateur'] != self.cryption_tools.crypt_sha256(password)):

                    return {'status': 'failed', 'message': 'Utilisateur Non Trouvé'}
                if user[0]['compte_utilisateur'] == 'Banni':
                    return {'status': 'failed', 'message': 'Utilisateur Désactivé'}
                if user[0]['compte_utilisateur'] == 'Pas Encore Confirmé':
                    return {'status': 'failed', 'message': 'Utilisateur Non Confirmé'}
                user[0].pop('mdp_utilisateur')
                session['user'] = user[0]
                return {'status': 'success', 'user': user[0]}
            elif status == 'failed' or user is None or user == []:

                return {'status': 'failed', 'message': 'Utilisateur Non Trouvé'}
            else:
                return {'status': 'error', 'message': 'Erreur Serveur'}

        @self.auth_bp.route('/logout', methods=['GET'])
        def logout():
            session['user'] = None
            return redirect(url_for('auth.login'))

        @self.auth_bp.route('/mot-de-passe-oublie', methods=['GET'])
        def forgot_password():
            return render_template('client/forgotten-password.html')


if __name__ == '__main__':
    pass
