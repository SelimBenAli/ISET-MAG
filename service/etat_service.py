from entities.etat import Etat
from tools.database_tools import DatabaseConnection


class EtatService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_etat_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDEtat`, `Nom`, `Description` FROM etat WHERE {add}""")
            data = self.cursor.fetchall()
            liste_etat = []
            for element in data:
                etat = Etat(element[0], element[1], element[2])
                liste_etat.append(etat.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_etat
        except Exception as e:
            return 'error', e

    def find_all_etat(self):
        return self.find_etat_by_something(' 1')

    def find_etat_by_id(self, id_etat):
        return self.find_etat_by_something(f' IDEtat = {id_etat}')

    def find_etat_by_nom(self, nom):
        return self.find_etat_by_something(f" Nom LIKE '%{nom}%'")

    def add_etat(self, nom, description):
        return self.database_tools.execute_request(
            f"""INSERT INTO etat (Nom, Description) VALUES ('{nom}', '{description}')""")

    def update_etat(self, id_etat, nom, description):
        return self.database_tools.execute_request(
            f"""UPDATE etat SET Nom = '{nom}', Description = '{description}' WHERE IDEtat = {id_etat}""")

    def delete_etat(self, id_etat):
        return self.database_tools.execute_request(f"""DELETE FROM etat WHERE IDEtat = {id_etat}""")


if __name__ == '__main__':
    pass
