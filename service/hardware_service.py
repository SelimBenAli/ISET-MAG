import json

from entities.hardware import Hardware
from service.etat_service import EtatService
from service.fournisseur_service import FournisseurService
from service.magasin_service import MagasinService
from service.modele_service import ModeleService
from service.relation_service import RelationService
from service.salle_service import SalleService
from tools.database_tools import DatabaseConnection
from tools.date_tools import DateTools


class HardwareService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()
        self.date_tools = DateTools()

    def find_hardware_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            req = (
                f"""SELECT IDHardware, IDModel, IDFournisseur, IDMagasin, IDSalle, IDEtat,
                NumeroInventaire, DateAchat, DateAjout, DateMiseEnService, 
                Code, HistoriqueRelation FROM hardware WHERE MarkedAsDeleted = -1 AND {add}""")

            self.cursor.execute(req)
            data = self.cursor.fetchall()
            liste_hardware = []
            for element in data:
                status, modele = ModeleService().find_modele_by_id(element[1])
                # status, relation = RelationService().find_relation_by_hardware(element[0])
                status, magasin = MagasinService().find_magasin_by_id(element[3])
                if status == 'error':
                    magasin = MagasinService().create_none().dict_form()
                else:
                    magasin = magasin[0]
                status, salle = SalleService().find_salle_by_id(element[4])
                if status == 'error':
                    salle = SalleService().create_none().dict_form()
                else:
                    salle = salle[0]
                status, etat = EtatService().find_etat_by_id(element[5])
                status, fournisseur = FournisseurService().find_fournisseur_by_id(element[2])
                if status == 'error':
                    fournisseur = FournisseurService().create_none().dict_form()
                else:
                    fournisseur = fournisseur[0]

                hardware = Hardware(element[0], modele[0], fournisseur, magasin, salle, etat[0], element[6],
                                    self.date_tools.convert_date(element[7]),
                                    self.date_tools.convert_date(element[9]),
                                    self.date_tools.convert_date(element[8]),
                                    element[10], None)

                liste_hardware.append(hardware.dict_form())
            self.cursor.close()
            self.connection.close()
            return 'success', liste_hardware
        except Exception as e:
            return 'error', e

    def find_all_hardware(self):
        return self.find_hardware_by_something(" 1")

    def find_all_hardware_with_limit(self, number, begin):
        return self.find_hardware_by_something(" 1 LIMIT " + str(begin) + ", " + str(number))

    def find_hardware_by_id(self, id_hardware):
        return self.find_hardware_by_something(f" IDHardware = {id_hardware} ")

    def find_hardware_by_modele(self, id_modele):
        return self.find_hardware_by_something(f" IDModel = {id_modele} ")

    def find_hardware_by_fournisseur(self, id_fournisseur):
        return self.find_hardware_by_something(f" IDFournisseur = {id_fournisseur} ")

    def find_hardware_by_magasin(self, id_magasin):
        return self.find_hardware_by_something(f" IDMagasin = {id_magasin} ")

    def find_hardware_by_salle(self, id_salle):
        return self.find_hardware_by_something(f" IDSalle = {id_salle} ")

    def find_hardware_by_numero_inventaire(self, numero_inventaire):
        return self.find_hardware_by_something(f" NumeroInventaire = '{numero_inventaire}' ")

    def find_hardware_by_date_achat(self, date_achat):
        return self.find_hardware_by_something(f" DateAchat = {date_achat} ")

    def find_hardware_by_date_mise_en_service(self, date_mise_en_service):
        return self.find_hardware_by_something(f" DateMiseEnService = {date_mise_en_service} ")

    def find_hardware_by_code(self, code):
        return self.find_hardware_by_something(f" Code = '{code}' ")

    # NOT FOUND
    def find_hardware_by_historique_relation(self, historique_relation):
        ...

    def add_hardware(self, id_model, id_fournisseur, id_magasin, id_salle, numero_inventaire, date_achat,
                     date_mise_en_service, code, id_etat, historique_relation):

        add = ''
        if date_achat == 'NULL' or date_achat == ' NULL ':
            add += " NULL, NOW(), "
        else:
            add += f"'{date_achat}', NOW(), "
        if date_mise_en_service == 'NULL' or date_mise_en_service == ' NULL ':
            add += " NULL "
        else:
            add += f"'{date_mise_en_service}' "
        req = (f"""INSERT INTO hardware (IDModel, IDFournisseur, IDMagasin, IDSalle, 
         NumeroInventaire, DateAchat, DateAjout, DateMiseEnService, Code, IDEtat, HistoriqueRelation) 
                VALUES ({id_model}, {id_fournisseur}, {id_magasin}, {id_salle}, '{numero_inventaire}', {add}, '{code}', {id_etat}, {json.dumps(historique_relation)})""")

        return self.database_tools.execute_request(req)

    def update_hardware(self, id_hardware, id_model, id_fournisseur, id_magasin, id_salle, numero_inventaire,
                        date_achat,
                        date_mise_en_service, code, id_etat, historique_relation):
        add = ''
        if date_achat == 'NULL' or date_achat == ' NULL ':
            add += " DateAchat = NULL, "
        else:
            add += f" DateAchat = '{date_achat}', "
        if date_mise_en_service == 'NULL' or date_mise_en_service == ' NULL ':
            add += " DateMiseEnService = NULL "
        else:
            add += f" DateMiseEnService = '{date_mise_en_service}' "
        req = (
            f"""UPDATE hardware SET IDModel = {id_model}, IDFournisseur = {id_fournisseur},
                 IDMagasin = {id_magasin}, IDSalle = {id_salle}, NumeroInventaire = '{numero_inventaire}', {add},
                 Code = '{code}', IDEtat = {id_etat},
                   HistoriqueRelation = {json.dumps(historique_relation)}
                   WHERE IDHardware = {id_hardware}""")

        return self.database_tools.execute_request(req)

    def delete_hardware(self, id_hardware):
        return self.database_tools.execute_request(f"""UPDATE hardware SET MarkedAsDeleted 
        WHERE IDHardware = {id_hardware}""")

    def find_number_hardware(self):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(f"""SELECT COUNT(IDHardware) FROM hardware""")
            data = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            return 'success', data[0][0]
        except Exception as e:
            return 'error', e


if __name__ == '__main__':
    pass
