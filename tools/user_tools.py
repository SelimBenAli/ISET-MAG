from flask import session

from service.admin_service import AdminService
from tools.database_tools import DatabaseConnection


class UserTools:
    def __init__(self):
        self.connection_tools = DatabaseConnection()
        self.admin_service = AdminService()

    def refresh_session(self, user):
        status, admin = self.admin_service.find_admin_by_id(user['id_admin'])
        print(admin)
        if status == 'success':
            session['admin'] = admin
        return admin

    def check_user_in_session(self, user):
        if user not in session or not session[user] or session[user] == "" or session[user] is None:
            return False
        print(user, session[user])
        na = self.refresh_session(session[user])
        print(na)
        if na is None:
            return False
        if na['marked_as_deleted'] == 1:
            return False
        if na['desactive_admin'] == 1:
            return False
        return True
