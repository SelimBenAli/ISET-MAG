from flask import session

from service.admin_service import AdminService
from service.utilisateur_service import UtilisateurService
from tools.database_tools import DatabaseConnection


class UserTools:
    def __init__(self):
        self.connection_tools = DatabaseConnection()
        self.admin_service = AdminService()
        self.utilisateur_service = UtilisateurService()

    def refresh_session_admin(self, user):
        status, admin = self.admin_service.find_admin_by_id(user['id_admin'])
        print(admin)
        if status == 'success':
            session['admin'] = admin
        return admin

    def refresh_session_user(self, user):
        status, user = self.utilisateur_service.find_utilisateur_by_id(user['id_utilisateur'])
        print('new user : ', user)
        if status == 'success':
            session['user'] = user[0]
        return user[0]

    def check_user_in_session(self, user):
        if user not in session or not session[user] or session[user] == "" or session[user] is None:
            return False
        print(user, session[user])
        if user == 'admin':
            na = self.refresh_session_admin(session[user])
            print("na", na)
            if na is None:
                return False
            if na['marked_as_deleted'] == 1:
                return False
            if na['desactive_admin'] == 1:
                return False
        else:
            na = self.refresh_session_user(session[user])
            print("na", na)
            if na is None:
                return False
            if na['marked_as_deleted'] == 1:
                return False
            if na['compte_utilisateur'] != 'Active':
                return False
        return True
