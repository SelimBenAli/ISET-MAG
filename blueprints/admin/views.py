from flask import Blueprint, render_template, request, session, redirect, url_for

from service.admin_service import AdminService
from tools.scanner_tools import ScannerTools
from tools.user_tools import UserTools
from extensions import socketio


class AdminViews:
    def __init__(self):
        self.admin_service = AdminService()
        self.user_tools = UserTools()
        self.scan_tools = ScannerTools()
        self.admin_bp = Blueprint('admin', __name__, template_folder='templates')
        self.admin_routes()
        # commentaire

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
                admin = admin.dict_form()
                print(admin)
                if admin['desactive_admin'] == 1:
                    return {'status': 'failed', 'message': 'Votre Compte est Désactivé'}
                if admin['marked_as_deleted'] == 1:
                    return {'status': 'failed', 'message': 'Utilisateur Non Trouvé'}
                print("ok", admin)
                session['admin'] = admin
                self.scan_tools.switch_scan_ending('doubleEnter')
                return {'status': 'success'}
            elif status == 'failed':
                print("no")
                return {'status': 'failed', 'message': 'Utilisateur Non Trouvé'}
            else:
                return {'status': 'Error'}

        @self.admin_bp.route('/logout', methods=['GET'])
        def logout():
            session['admin'] = None
            self.scan_tools.clear_scan_ending()
            return redirect(url_for('admin.login'))

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

        @self.admin_bp.route('/activate-admin/<int:ida>', methods=['PUT'])
        def activate_admin(ida):
            if self.user_tools.check_user_in_session('admin'):
                status = self.admin_service.activate_admin(ida)
                if status == 'success':
                    return {'status': 'success'}
                return {'status': 'failed'}
            return {'status': 'failed'}

        @self.admin_bp.route('/add-admin', methods=['POST'])
        def add_admin():
            if self.user_tools.check_user_in_session('admin'):
                data = request.get_json()
                nom = data.get('nom_admin')
                prenom = data.get('prenom_admin')
                email = data.get('email_admin')
                status = self.admin_service.add_admin(nom, prenom, email, 2)
                if status == 'success':
                    return {'status': 'success'}
                return {'status': 'failed'}
            return {'status': 'failed'}

        @self.admin_bp.route('/delete-admin/<int:ida>', methods=['DELETE'])
        def delete_admin(ida):
            if self.user_tools.check_user_in_session('admin'):
                status = self.admin_service.delete_admin(ida)
                if status == 'success':
                    return {'status': 'success'}
                return {'status': 'failed'}
            return {'status': 'failed'}
