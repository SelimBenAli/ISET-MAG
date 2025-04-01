from entities.magasin import Magasin
from service.salle_service import SalleService
from tools.database_tools import DatabaseConnection


class MagasinService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_magasin_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDMagasin`, `Nom`, `IDSalle` FROM magasin WHERE {add}""")
            data = self.cursor.fetchall()
            liste_magasin = []
            for element in data:
                salle = SalleService().find_salle_by_id(element[2])[1][0]
                magasin = Magasin(element[0], element[1], salle)
                liste_magasin.append(magasin.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_magasin
        except Exception as e:
            return 'error', e

    def find_all_magasin(self):
        return self.find_magasin_by_something(' 1')

    def find_magasin_by_id(self, id_magasin):
        return self.find_magasin_by_something(f' IDMagasin = {id_magasin}')

    def find_magasin_by_salle(self, id_salle):
        return self.find_magasin_by_something(f" IDSalle = '{id_salle}'")

    def find_magasin_by_nom(self, nom):
        return self.find_magasin_by_something(f" Nom LIKE '%{nom}%'")

    def add_magasin(self, nom, id_salle):
        return self.database_tools.execute_request(
            f"""INSERT INTO magasin (Nom, IDSalle) VALUES ('{nom}', {id_salle})""")

    def update_magasin(self, id_magasin, id_salle, nom):
        return self.database_tools.execute_request(
            f"""UPDATE magasin SET IDSalle = '{id_salle}', Nom = '{nom}' WHERE IDMagasin = {id_magasin}""")

    def delete_magasin(self, id_magasin):
        return self.database_tools.execute_request(f"""DELETE FROM magasin WHERE IDMagasin = {id_magasin}""")

    @staticmethod
    def create_none():
        return Magasin(None, None, None)


if __name__ == '__main__':
    pass
