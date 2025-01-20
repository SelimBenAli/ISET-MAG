from entities.fournisseur import Fournisseur
from tools.database_tools import DatabaseConnection


class FournisseurService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_fournisseur_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDFournisseur`, `Nom`, `Tel` FROM fournisseur WHERE {add}""")
            data = self.cursor.fetchall()
            liste_fournisseur = []
            for element in data:
                fournisseur = Fournisseur(element[0], element[1], element[2])
                liste_fournisseur.append(fournisseur.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_fournisseur
        except Exception as e:
            return 'error', e

    def find_fournisseur_by_id(self, id_fournisseur):
        return self.find_fournisseur_by_something(f' IDFournisseur = {id_fournisseur}')

    def find_all_fournisseur(self):
        return self.find_fournisseur_by_something(' 1')

    def find_fournisseur_by_nom(self, nom):
        return self.find_fournisseur_by_something(f" Nom LIKE '%{nom}%'")

    def find_fournisseur_by_tel(self, tel):
        return self.find_fournisseur_by_something(f" Tel LIKE '%{tel}%'")

    def add_fournisseur(self, nom, tel):
        return self.database_tools.execute_request(f"""INSERT INTO fournisseur (Nom, Tel) VALUES ('{nom}', '{tel}')""")

    def update_fournisseur(self, id_fournisseur, nom, tel):
        return self.database_tools.execute_request(
            f"""UPDATE fournisseur SET Nom = '{nom}', Tel = '{tel}' WHERE IDFournisseur = {id_fournisseur}""")

    def delete_fournisseur(self, id_fournisseur):
        return self.database_tools.execute_request(f"""DELETE FROM fournisseur WHERE IDFournisseur = {id_fournisseur}""")
