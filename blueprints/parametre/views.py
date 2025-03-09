from flask import Blueprint, render_template, request, session, flash, url_for, redirect

from service.parametre_email_service import ParametreEmailService
from tools.cryption_tools import CryptionTools
from tools.user_tools import UserTools


class ParametreEmailViews:
    def __init__(self):
        self.user_tools = UserTools('dashboard')
        self.cryption_tools = CryptionTools()
        self.parametre_email_service = ParametreEmailService()
        self.parametre_bp = Blueprint('parametre', __name__, template_folder='templates')
        self.parametre_routes()

    def parametre_routes(self):
        @self.parametre_bp.route('/parametre-email-update/<int:id_parametre_email>', methods=['PUT'])
        def parametre_email_update(id_parametre_email):
            if not self.user_tools.check_user_in_session('user'):
                return redirect(url_for('auth.login'))
            data = request.get_json()
            nom = data.get('nom')
            objet = data.get('objet')
            text = data.get('text')
            status, message = self.parametre_email_service.update_parametre_email(id_parametre_email, nom, objet, text)
            if status == 'success':
                return {'status': 'success', 'message': message}
            else:
                return {'status': 'error', 'message': message}
