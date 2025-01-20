from entities.role import Role
from tools.database_tools import DatabaseConnection


class RoleService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_role_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDRole`, `Nom` FROM role WHERE {add}""")
            data = self.cursor.fetchall()
            liste_role = []
            for element in data:
                role = Role(element[0], element[1])
                liste_role.append(role.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_role
        except Exception as e:
            return 'error', e

    def find_role_by_id(self, id_role):
        return self.find_role_by_something(f" IDRole = {id_role}")

    def find_all_role(self):
        return self.find_role_by_something(" 1")

    def find_role_by_nom(self, nom):
        return self.find_role_by_something(f" Nom LIKE '%{nom}%'")

    def add_role(self, nom):
        return self.database_tools.execute_request(f"""INSERT INTO role (Nom) VALUES ('{nom}')""")

    def update_role(self, id_role, nom):
        return self.database_tools.execute_request(f"""UPDATE role SET Nom = '{nom}' WHERE IDRole = {id_role}""")

    def delete_role(self, id_role):
        return self.database_tools.execute_request(f"""DELETE FROM role WHERE IDRole = {id_role}""")
