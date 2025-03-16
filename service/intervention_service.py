from entities.intervention import Intervention
from service.admin_service import AdminService
from service.hardware_service import HardwareService
from service.salle_service import SalleService
from service.utilisateur_service import UtilisateurService
from tools.database_tools import DatabaseConnection
from tools.date_tools import DateTools


class InterventionService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()
        self.date_tools = DateTools()

    def find_intervention_by_something(self, add, limit=''):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDIntervention`, `IDUtilisateur`, `DateDebut`, `DateFin`, `IDSalle`,
                 `IDHardware`, `IDAdmin`, `IDAdminFermeture` FROM `intervention` WHERE {add} ORDER BY DateDebut DESC {limit}""")
            data = self.cursor.fetchall()
            liste_intervention = []
            for element in data:
                status, utilisateur = UtilisateurService().find_utilisateur_by_id(element[1])
                if element[4] is not None:
                    status, salle = SalleService().find_salle_by_id(element[4])
                    salle = salle[0]
                else:
                    salle = SalleService.create_none().dict_form()
                status, hardware = HardwareService().find_hardware_by_id(element[5])
                status, admin = AdminService().find_admin_by_id(element[6])
                admin_fermeture = None
                if element[7] is not None:
                    status, admin_fermeture = AdminService().find_admin_by_id(element[7])
                intervention = Intervention(element[0], utilisateur[0], salle, hardware[0], admin,
                                            self.date_tools.convert_date_time(element[2]),
                                            self.date_tools.convert_date_time(element[3]), admin_fermeture)
                liste_intervention.append(intervention.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_intervention
        except Exception as e:
            return 'error', e

    def find_all_intervention(self):
        return self.find_intervention_by_something(' 1')

    def find_all_intervention_with_limit(self, conditions, begin, number):
        print(begin, number, "aa444")
        return self.find_intervention_by_something(f" 1 {conditions} ", f"LIMIT {begin}, {number}")

    def find_intervention_by_id(self, id_intervention):
        return self.find_intervention_by_something(f' IDIntervention = {id_intervention}')

    def find_intervention_by_user(self, id_user, limit=''):
        return self.find_intervention_by_something(f' IDUtilisateur = {id_user}', limit)

    def find_intervention_not_closed_by_user(self, id_user, limit=''):
        return self.find_intervention_by_something(f' IDUtilisateur = {id_user} AND DateFin IS NULL', limit)

    def find_intervention_by_salle(self, id_salle):
        return self.find_intervention_by_something(f' IDSalle = {id_salle}')

    def find_intervention_by_hardware(self, id_hardware):
        return self.find_intervention_by_something(f' IDHardware = {id_hardware}')

    def find_intervention_by_used_hardware(self, id_hardware):
        return self.find_intervention_by_something(f' IDHardware = {id_hardware} AND DateFin IS NULL')

    def find_intervention_by_admin(self, id_admin, begin, number):
        return self.find_intervention_by_something(f' IDAdmin = {id_admin}, ', f'LIMIT {begin}, {number}')

    def find_intervention_closed(self):
        return self.find_intervention_by_something(' DateFin IS NOT NULL')

    def find_intervention_open(self):
        return self.find_intervention_by_something(' DateFin IS NULL')

    def add_intervention(self, id_user, date_debut, date_fin, id_salle, id_hardware, id_admin):
        return self.database_tools.execute_request(
            f"""INSERT INTO intervention (IDUtilisateur, DateDebut, DateFin, IDSalle, IDHardware, IDAdmin) 
            VALUES ({id_user}, NOW(), NULL, NULL, {id_hardware}, {id_admin})""")

    def update_intervention(self, id_intervention, id_user, date_debut, id_salle, id_hardware):
        return self.database_tools.execute_request(
            f"""UPDATE intervention SET IDUtilisateur = {id_user}, DateDebut = '{date_debut}',
             IDSalle = {id_salle}, IDHardware = {id_hardware} 
              WHERE IDIntervention = {id_intervention}""")

    def delete_intervention(self, id_intervention):
        return self.database_tools.execute_request(f"""DELETE FROM intervention 
        WHERE IDIntervention = {id_intervention}""")

    def close_intervention(self, id_intervention, id_admin):
        return self.database_tools.execute_request(
            f"""UPDATE intervention SET DateFin = NOW(), IDAdminFermeture = '{id_admin}' 
            WHERE IDIntervention = {id_intervention}""")

    def find_number_interventions(self, conditions):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(f"""SELECT COUNT(*) FROM intervention WHERE 1 {conditions}""")
            data = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            return 'success', data[0][0]
        except Exception as e:
            return 'error', e

    def find_number_current_interventions(self):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(f"""SELECT COUNT(*) FROM intervention WHERE DateFin IS NULL""")
            data = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            return 'success', data[0][0]
        except Exception as e:
            return 'error', e

    def find_current_intervention_with_limit(self, begin, number):
        return self.find_intervention_by_something("  DateFin IS NULL ", f"LIMIT {begin}, {number}")

    def find_number_closed_interventions(self):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(f"""SELECT COUNT(*) FROM intervention WHERE DateFin IS NOT NULL""")
            data = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            return 'success', data[0][0]
        except Exception as e:
            return 'error', e

    def find_closed_intervention_with_limit(self, begin, number):
        return self.find_intervention_by_something("  DateFin IS NOT NULL ", f"LIMIT {begin}, {number}")
