from entities.modele import Modele
from service.marque_service import MarqueService
from tools.database_tools import DatabaseConnection


class ModeleService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_modele_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDModel`, `Nom`, `IDMarque` FROM model_hardware WHERE {add}""")
            data = self.cursor.fetchall()
            liste_modele = []
            for element in data:
                if element[2] is None:
                    marque = MarqueService().create_none().dict_form()
                else:
                    status, marque = MarqueService().find_marque_by_id(element[2])
                    marque = marque[0]
                modele = Modele(element[0], element[1], marque)
                liste_modele.append(modele.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_modele
        except Exception as e:
            return 'error', e


    def find_all_modele(self):
        return self.find_modele_by_something(' 1')

    def find_modele_by_id(self, id_modele):
        return self.find_modele_by_something(f' IDModel = {id_modele}')

    def find_modele_by_marque(self, id_marque):
        return self.find_modele_by_something(f' IDMarque = {id_marque}')

    def find_modele_by_nom(self, nom):
        return self.find_modele_by_something(f" Nom LIKE '%{nom}%'")

    def add_modele(self, nom, id_marque):
        return self.database_tools.execute_request(
            f"""INSERT INTO model_hardware (Nom, IDMarque) VALUES ('{nom}', {id_marque})""")

    def delete_modele(self, id_modele):
        return self.database_tools.execute_request(f"""DELETE FROM model_hardware WHERE IDModel = {id_modele}""")

    def update_modele(self, id_modele, nom, id_marque):
        return self.database_tools.execute_request(
            f"""UPDATE model_hardware SET Nom = '{nom}', IDMarque = {id_marque} WHERE IDModel = {id_modele}""")
