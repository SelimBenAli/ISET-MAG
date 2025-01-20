from entities.bloc import Bloc
from tools.database_tools import DatabaseConnection


class BlocService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_bloc_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDBloc`, `Nom` FROM bloc WHERE {add}""")
            data = self.cursor.fetchall()
            liste_bloc = []
            for element in data:
                bloc = Bloc(element[0], element[1])
                liste_bloc.append(bloc.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_bloc
        except Exception as e:
            return 'error', e

    def find_bloc_by_id(self, id_bloc):
        return self.find_bloc_by_something(f' IDBloc = {id_bloc}')

    def find_all_bloc(self):
        return self.find_bloc_by_something(' 1')

    def add_bloc(self, nom):
        return self.database_tools.execute_request(f"""INSERT INTO bloc (Nom) VALUES ('{nom}')""")

    def update_bloc(self, id_bloc, nom):
        return self.database_tools.execute_request(f"""UPDATE bloc SET Nom = '{nom}' WHERE IDBloc = {id_bloc}""")

    def delete_bloc(self, id_bloc):
        return self.database_tools.execute_request(f"""DELETE FROM bloc WHERE IDBloc = {id_bloc}""")
