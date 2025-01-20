from flask import session

from tools.database_tools import DatabaseConnection


class UserTools:
    def __init__(self):
        self.connection_tools = DatabaseConnection()

    @staticmethod
    def check_user_in_session(user):
        if user not in session or not session[user] or session[user] == "" or session[user] is None:
            return False
        print(user, session[user])
        return True
