from entities.marque import Marque
from tools.database_tools import DatabaseConnection


class MarqueService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_marque_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDMarque`, `Nom` FROM marque WHERE {add}""")
            data = self.cursor.fetchall()
            liste_marque = []
            for element in data:
                marque = Marque(element[0], element[1])
                liste_marque.append(marque.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_marque
        except Exception as e:
            return 'error', e

    def find_all_marque(self):
        return self.find_marque_by_something(' 1')

    def find_marque_by_id(self, id_marque):
        return self.find_marque_by_something(f' IDMarque = {id_marque}')

    def find_marque_by_nom(self, nom):
        return self.find_marque_by_something(f" Nom LIKE '%{nom}%'")

    def add_marque(self, nom):
        return self.database_tools.execute_request(f"""INSERT INTO marque (Nom) VALUES ('{nom}')""")

    def update_marque(self, id_marque, nom):
        return self.database_tools.execute_request(
            f"""UPDATE marque SET Nom = '{nom}' WHERE IDMarque = {id_marque}""")

    def delete_marque(self, id_marque):
        return self.database_tools.execute_request(f"""DELETE FROM marque WHERE IDMarque = {id_marque}""")
