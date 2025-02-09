from flask import Blueprint, render_template, request, session, flash

from service.admin_service import AdminService
from tools.user_tools import UserTools
from extensions import socketio


class AdminViews:
    def __init__(self):
        self.admin_service = AdminService()
        self.user_tools = UserTools()
        self.admin_bp = Blueprint('admin', __name__, template_folder='templates')
        self.admin_routes()

    def admin_routes(self):
        @self.admin_bp.route('/login', methods=['GET'])
        def login():
            return render_template('admin-login.html')

        @self.admin_bp.route('/login', methods=['POST'])
        def login_post():
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            status, admin = self.admin_service.find_admin(email, password)
            print(status)
            if status == 'success':
                if admin['desactive_admin'] == 1:
                    flash('Votre Compte est Désactivé', 'error')
                    return {'status': 'failed'}
                if admin['marked_as_deleted'] == 1:
                    flash('Votre Compte est Supprimé', 'error')
                    return {'status': 'failed'}
                print("ok", admin)
                session['admin'] = admin.dict_form()
                return {'status': 'success'}
            elif status == 'failed':
                print("no")
                flash('Utilisateur Non Trouvé', 'error')
                return {'status': 'failed'}
            else:
                flash('Erreur Serveur', 'error')
                return {'status': 'error'}

        @self.admin_bp.route('/logout', methods=['GET'])
        def logout():
            session['admin'] = None
            return render_template('admin-login.html')

        @self.admin_bp.route('/change-details', methods=['PUT'])
        def change_details():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                id_admin = session['admin']['id_admin']
                email = data.get('email')
                prenom = data.get('prenom')
                nom = data.get('nom')
                status = self.admin_service.change_details(id_admin, prenom, nom, email)
                if status == 'success':
                    return {'status': 'success'}
                return {'status': 'failed'}
            return {'status': 'failed'}

        @self.admin_bp.route('/load-page-admins', methods=['GET'])
        def load_page_admins():
            if self.user_tools.check_user_in_session('admin'):
                status, admins = self.admin_service.find_all_admin()
                if status == 'success':
                    return {'status': 'success', 'admins': admins}
                return {'status': 'failed'}
            return {'status': 'failed'}

        @self.admin_bp.route('/desactivate-admin/<int:ida>', methods=['PUT'])
        def desactivate_admin(ida):
            if self.user_tools.check_user_in_session('admin'):
                status = self.admin_service.desactivate_admin(ida)
                if status == 'success':
                    socketio.emit('close_admin_session', {'message': 'success', 'id_admin': ida})
                    return {'status': 'success'}
                return {'status': 'failed'}
            return {'status': 'failed'}
