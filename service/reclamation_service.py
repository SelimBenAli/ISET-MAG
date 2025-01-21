from entities.reclamation import Reclamation
from service.etat_service import EtatService
from service.hardware_service import HardwareService
from service.intervention_service import InterventionService
from service.utilisateur_service import UtilisateurService
from tools.database_tools import DatabaseConnection


class ReclamationService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_reclamation_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDReclamation`, `IDHardware`, `IDUtilisateur`, `IDIntervention`, `DateReclamation`,
                 `Description`, `IDEtat` FROM `reclamation_hardware` WHERE {add}""")
            data = self.cursor.fetchall()
            liste_reclamation = []
            for element in data:
                hardware = HardwareService().find_hardware_by_id(element[1])
                utilisateur = UtilisateurService().find_utilisateur_by_id(element[2])
                intervention = InterventionService().find_intervention_by_id(element[3])
                etat = EtatService().find_etat_by_id(element[6])
                reclamation = Reclamation(
                    element[0], hardware, utilisateur, intervention, element[4], element[5], etat
                )
                liste_reclamation.append(reclamation)
            self.cursor.close()
            self.connection.close()
            return 'success', liste_reclamation
        except Exception as e:
            return 'error', e

    def find_reclamation_by_id(self, id_reclamation):
        return self.find_reclamation_by_something(f" IDReclamation = {id_reclamation}")

    def find_all_reclamation(self):
        return self.find_reclamation_by_something(" 1")

    def find_reclamation_by_id_utilisateur(self, id_utilisateur):
        return self.find_reclamation_by_something(f" IDUtilisateur = {id_utilisateur}")

    def find_reclamation_by_id_intervention(self, id_intervention):
        return self.find_reclamation_by_something(f" IDIntervention = {id_intervention}")

    def find_reclamation_by_id_etat(self, id_etat):
        return self.find_reclamation_by_something(f" IDEtat = {id_etat}")

    def add_reclamation(self, id_hardware, id_utilisateur, id_intervention, description):
        return self.database_tools.execute_request(
            f"""INSERT INTO reclamation_hardware (IDHardware, IDUtilisateur, IDIntervention, 
             Description, IDEtat) 
            VALUES ({id_hardware}, {id_utilisateur}, {id_intervention}, "{description}",
             NULL)""")

    def update_reclamation(self, id_reclamation, id_hardware, id_utilisateur, id_intervention, date_reclamation,
                           description, id_etat):
        return self.database_tools.execute_request(
            f"""UPDATE reclamation_hardware SET IDHardware = {id_hardware},
             IDUtilisateur = {id_utilisateur}, IDIntervention = {id_intervention}, 
            DateReclamation = '{date_reclamation}', Description = '{description}', 
            IDEtat = {id_etat} WHERE IDReclamation = {id_reclamation}""")

    def delete_reclamation(self, id_reclamation):
        return self.database_tools.execute_request(
            f"DELETE FROM reclamation_hardware WHERE IDReclamation = {id_reclamation}")
