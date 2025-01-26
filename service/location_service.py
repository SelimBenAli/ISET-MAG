from service.admin_service import AdminService
from service.modele_service import ModeleService
from service.utilisateur_service import UtilisateurService
from tools.database_tools import DatabaseConnection
from entities.location import Location
from tools.date_tools import DateTools


class LocationService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()
        self.date_tools = DateTools()

    def find_location_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDLocation`, `DateDebutEstime`, `DateFinEstimee`, `IDUtilisateur`, `IDModel`, `Quantite`,
                 `Confirmation`, `IDAdmin`, `DateConfirmation` FROM `louer_hardware` WHERE {add} 
                 ORDER BY IDLocation DESC""")
            data = self.cursor.fetchall()
            liste_location = []
            for element in data:
                status, utilisateur = UtilisateurService().find_utilisateur_by_id(element[3])
                status, modele = ModeleService().find_modele_by_id(element[4])
                status, admin = AdminService().find_admin_by_id(element[7])
                if status != 'success':
                    admin = None
                location = Location(element[0], str(self.date_tools.convert_date_time(element[1])),
                                    str(self.date_tools.convert_date_time(element[2])), utilisateur[0], modele[0], admin,
                                    element[5],
                                    element[6],
                                    element[8])
                liste_location.append(location.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_location
        except Exception as e:
            return 'error', e

    def find_all_location(self):
        return self.find_location_by_something(' 1')

    def find_location_by_id(self, id_location):
        return self.find_location_by_something(f' IDLocation = {id_location}')

    def find_location_by_utilisateur(self, id_utilisateur):
        return self.find_location_by_something(f' IDUtilisateur = {id_utilisateur}')

    def find_location_by_hardware(self, id_hardware):
        return self.find_location_by_something(f' IDHardware = {id_hardware}')

    def find_location_by_confirmation(self, confirmation):
        return self.find_location_by_something(f' Confirmation = {confirmation}')

    def find_location_by_admin(self, id_admin):
        return self.find_location_by_something(f' IDAdmin = {id_admin}')

    def add_location(self, date_debut_estime, date_fin_estimee, id_utilisateur, id_modele, quantite):
        return self.database_tools.execute_request(
            f"""INSERT INTO louer_hardware (`IDLocation`, `DateDebutEstime`, `DateFinEstimee`, `IDUtilisateur`,
             `IDModel`, `Quantite`, `Confirmation`, `IDAdmin`, `DateConfirmation`) VALUES
              (NULL, '{date_debut_estime}', '{date_fin_estimee}', 
            {id_utilisateur}, {id_modele}, {quantite}, 0, NULL, NULL)""")

    def update_location(self, id_location, date_debut_estime, date_fin_estimee, id_utilisateur, id_modele, quantite,
                        confirmation, id_admin, date_confirmation):
        return self.database_tools.execute_request(
            f"""UPDATE louer_hardware SET DateDebutEstime = '{date_debut_estime}', 
            DateFinEstimee = '{date_fin_estimee}', IDUtilisateur = {id_utilisateur}, 
            IDModel = {id_modele}, Quantite = {quantite}, Confirmation = {confirmation}, 
            IDAdmin = {id_admin}, DateConfirmation = '{date_confirmation}' WHERE IDLocation = {id_location}""")

    def confirm_location(self, confirmation, id_location, id_admin):
        return self.database_tools.execute_request(
            f"""UPDATE louer_hardware SET Confirmation = '{confirmation}', IDAdmin = '{id_admin}',
            DateConfirmation = NOW() WHERE IDLocation = {id_location}""")

    def delete_location(self, id_location):
        return self.database_tools.execute_request(f"""DELETE FROM louer_hardware WHERE IDLocation = {id_location}""")
