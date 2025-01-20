from tools.database_tools import DatabaseConnection
from entities.admin import Admin


class AdminService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_admin(self, email, password):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            req = (
                f"""SELECT `IDAdmin`, `Nom`, `Prenom`, `Mail`, `MDP` FROM admin 
                WHERE Mail = '{email}' AND MDP = '{password}'""")
            print(req)
            self.cursor.execute(req)
            data = self.cursor.fetchone()
            self.cursor.close()
            self.connection.close()
            if data is None:
                return 'failed', 'Admin not found'
            else:
                admin = Admin(data[0], data[1], data[2], data[3], 'None')
            return 'success', admin
        except Exception as e:
            return 'error', e

    def find_admin_by_id(self, id_utilisateur):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDAdmin`, `Nom`, `Prenom`, `Mail`, `MDP` FROM admin 
                WHERE IDAdmin = '{id_utilisateur}'""")
            data = self.cursor.fetchone()
            self.cursor.close()
            self.connection.close()
            if data is None:
                return 'failed', 'Admin not found'
            else:
                admin = Admin(data[0], data[1], data[2], data[3], 'None')
            return 'success', admin.dict_form()
        except Exception as e:
            return 'error', e
