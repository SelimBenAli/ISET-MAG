from entities.utilisateur import Utilisateur
from service.role_service import RoleService
from tools.database_tools import DatabaseConnection


class UtilisateurService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_utilisateur_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            req = (
                f"""SELECT IDUtilisateur, Nom, Prenom, Mail, Tel, MDP, Role, Code, Compte, MarkedAsDeleted
                 FROM utilisateur WHERE {add} AND MarkedAsDeleted = -1""")
            self.cursor.execute(req)
            data = self.cursor.fetchall()
            liste_utilisateur = []
            for element in data:
                status, role = RoleService().find_role_by_id(element[6])
                utilisateur = Utilisateur(element[0], element[1], element[2], element[3], element[4],
                                          element[5], element[7], role[0], element[8], element[9])
                liste_utilisateur.append(utilisateur.dict_form())
            try:
                self.cursor.close()
                self.connection.close()
            except Exception as e:
                ...
            return 'success', liste_utilisateur
        except Exception as e:
            return 'error', e

    def find_all_utilisateur(self):
        return self.find_utilisateur_by_something(' 1')

    def find_utilisateur_by_id(self, id_utilisateur):
        return self.find_utilisateur_by_something(f' IDUtilisateur = {id_utilisateur}')

    def find_utilisateur_by_nom(self, nom):
        return self.find_utilisateur_by_something(f" Nom LIKE '%{nom}%'")

    def find_utilisateur_by_prenom(self, prenom):
        return self.find_utilisateur_by_something(f" Prenom LIKE '%{prenom}%'")

    def find_utilisateur_by_nom_prenom(self, string):
        return self.find_utilisateur_by_something(f" (Prenom LIKE '%{string}%' OR Nom LIKE '%{string}%') ")

    def find_utilisateur_by_mail(self, mail):
        return self.find_utilisateur_by_something(f" Mail LIKE '%{mail}%'")

    def find_utilisateur_by_tel(self, tel):
        return self.find_utilisateur_by_something(f" Tel LIKE '%{tel}%'")

    def find_utilisateur_by_role(self, role):
        return self.find_utilisateur_by_something(f" Role = '{role}'")

    def find_utilisateur_by_code(self, code):
        return self.find_utilisateur_by_something(f" Code LIKE '%{code}%'")

    def add_utilisateur(self, nom, prenom, mail, tel, mdp, role, code):
        return self.database_tools.execute_request(f"""INSERT INTO utilisateur (Nom, Prenom, Mail, Tel, MDP, Role, Code) 
                VALUES ('{nom}', '{prenom}', '{mail}', '{tel}', '{mdp}', '{role}', '{code}')""")

    def delete_utilisateur(self, id_utilisateur):
        return self.database_tools.execute_request(
            f"""UPDATE utilisateur SET MarkedAsDeleted = 1, Mail = NULL WHERE IDUtilisateur = {id_utilisateur}""")

    def update_utilisateur(self, id_utilisateur, nom, prenom, mail, tel, role, code):
        return self.database_tools.execute_request(
            f"""UPDATE utilisateur SET Nom = '{nom}', Prenom = '{prenom}', Mail = '{mail}',Tel = '{tel}', 
                Role = '{role}', Code = '{code}' WHERE IDUtilisateur = {id_utilisateur}""")

    def desactiver_compte(self, id_utilisateur):
        return self.database_tools.execute_request(
            f"""UPDATE utilisateur SET Compte = 2 WHERE IDUtilisateur = {id_utilisateur}""")

    def activer_compte(self, id_utilisateur):
        return self.database_tools.execute_request(
            f"""UPDATE utilisateur SET Compte = 1 WHERE IDUtilisateur = {id_utilisateur}""")

    def activer_tous_compte(self):
        return self.database_tools.execute_request(
            f"""UPDATE utilisateur SET Compte = 1 WHERE Compte = 2""")

    def desactiver_tous_compte(self):
        return self.database_tools.execute_request(
            f"""UPDATE utilisateur SET Compte = 2 WHERE Compte = 1""")
