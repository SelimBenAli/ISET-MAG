from entities.reclamation import Reclamation
from service.hardware_service import HardwareService
from service.intervention_service import InterventionService
from service.utilisateur_service import UtilisateurService
from tools.database_tools import DatabaseConnection
from tools.date_tools import DateTools


class ReclamationService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()
        self.date_tools = DateTools()

    def find_reclamation_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDReclamation`, `IDHardware`, `IDUtilisateur`, `IDIntervention`, `DateReclamation`,
                 `Description`, `IDEtat`, `Vu`, `IDTechnicien`, `DescriptionTechnicien`, `DateTechnicien`
                  FROM `reclamation_hardware` WHERE {add}""")
            data = self.cursor.fetchall()
            liste_reclamation = []
            for element in data:
                status, hardware = HardwareService().find_hardware_by_id(element[1])
                if element[8] == 'NULL' or element[8] is None:
                    technicien = None
                    description_technicien = None
                else:
                    status, technicien = UtilisateurService().find_utilisateur_by_id(element[8])
                    technicien = technicien[0]
                    description_technicien = element[9]
                status, utilisateur = UtilisateurService().find_utilisateur_by_id(element[2])
                status, intervention = InterventionService().find_intervention_by_id(element[3])
                if status == 'error':
                    intervention = None
                # etat = EtatService().find_etat_by_id(element[6])
                reclamation = Reclamation(
                    element[0], hardware[0], utilisateur[0], intervention, None, element[5],
                    self.date_tools.convert_date_time(element[4]), element[7], technicien, description_technicien,
                    self.date_tools.convert_date_time(element[10]))
                liste_reclamation.append(reclamation.dict_form())
            try:
                self.cursor.close()
                self.connection.close()
            except Exception as e:
                print(e)
            return 'success', liste_reclamation
        except Exception as e:
            return 'error', e

    def find_reclamation_by_id(self, id_reclamation):
        return self.find_reclamation_by_something(f" IDReclamation = {id_reclamation}")

    def find_all_reclamation(self):
        return self.find_reclamation_by_something(" 1 ORDER BY `DateReclamation` DESC")

    def find_reclamation_by_id_utilisateur(self, id_utilisateur):
        return self.find_reclamation_by_something(f" IDUtilisateur = {id_utilisateur}")

    def find_reclamation_by_id_intervention(self, id_intervention):
        return self.find_reclamation_by_something(f" IDIntervention = {id_intervention}")

    def find_reclamation_by_id_etat(self, id_etat):
        return self.find_reclamation_by_something(f" IDEtat = {id_etat}")

    def find_reclamation_by_not_finished(self):
        return self.find_reclamation_by_something(f" IDTechnicien IS NULL ")

    def add_reclamation(self, id_hardware, id_utilisateur, id_intervention, description):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""INSERT INTO reclamation_hardware (IDHardware, IDUtilisateur, IDIntervention, 
                 Description, IDEtat, Vu) 
                VALUES ({id_hardware}, {id_utilisateur}, {id_intervention}, "{description}",
                 NULL, '')""")
            self.connection.commit()
            lid = self.cursor.lastrowid
            try:
                self.cursor.close()
                self.connection.close()
            except Exception as e:
                print(e)
            return 'success', lid
        except Exception as e:
            return 'error', e

    def finish_reclamation(self, id_reclamation, id_technicien, description):
        return self.database_tools.execute_request(
            f""" UPDATE reclamation_hardware SET IDTechnicien = '{id_technicien}',
             DescriptionTechnicien = '{description}', DateTechnicien = NOW() 
             WHERE IDReclamation = '{id_reclamation}' AND IDTechnicien IS NULL"""
        )

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

    def add_seen_all_reclamation(self, id_utilisateur):
        self.connection, self.cursor = self.database_tools.find_connection()
        self.cursor.execute(
            f"""SELECT `IDReclamation`, `Vu` FROM reclamation_hardware WHERE `Vu` NOT LIKE "%{id_utilisateur}%;" """)
        liste_vues = self.cursor.fetchall()
        print(liste_vues)
        for liste_vu in liste_vues:
            print("aa : ", liste_vu)
            if liste_vu is not None:
                vues = liste_vu[1]
                id_reclamation = liste_vu[0]
                if vues is not None and vues != "":
                    my_list = str(vues) + f"{str(id_utilisateur)};"
                else:
                    my_list = f"{id_utilisateur};"
                req = (
                    f"""UPDATE reclamation_hardware SET Vu = '{my_list}' WHERE IDReclamation = {id_reclamation}""")
                print(req)
                self.database_tools.execute_request(req)
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
