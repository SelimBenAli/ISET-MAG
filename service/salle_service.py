from entities.salle import Salle
from service.bloc_service import BlocService
from tools.database_tools import DatabaseConnection


class SalleService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_salle_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDSalle`, `Nom`, `IDBloc` FROM salle WHERE
                  {add}""")
            data = self.cursor.fetchall()
            liste_salle = []
            for element in data:
                bloc = BlocService().find_bloc_by_id(element[2])[1]
                salle = Salle(element[0], element[1], bloc[0])
                liste_salle.append(salle.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_salle
        except Exception as e:
            return 'error', e

    def find_all_salle(self):
        return self.find_salle_by_something(' 1')

    def find_salle_by_id(self, id_salle):
        return self.find_salle_by_something(f' IDSalle = {id_salle}')

    def find_salle_by_bloc(self, id_bloc):
        return self.find_salle_by_something(f' IDBloc = {id_bloc}')

    def find_salle_by_nom(self, nom):
        return self.find_salle_by_something(f" Nom LIKE '%{nom}%'")

    def add_salle(self, nom, id_bloc):
        return self.database_tools.execute_request(f"""INSERT INTO salle (Nom, IDBloc) VALUES ('{nom}', {id_bloc})""")

    def update_salle(self, id_salle, nom, id_bloc):
        return self.database_tools.execute_request(
            f"""UPDATE salle SET Nom = '{nom}', IDBloc = {id_bloc} WHERE IDSalle = {id_salle}""")

    def delete_salle(self, id_salle):
        return self.database_tools.execute_request(f"""DELETE FROM salle WHERE IDSalle = {id_salle}""")

    @staticmethod
    def create_none():
        return Salle(None, None, None)
