from tools.admin_tools import AdminTools
from tools.cryption_tools import CryptionTools
from tools.database_tools import DatabaseConnection
from entities.admin import Admin
from tools.mail_tools import MailTools


class AdminService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()
        self.mail_tools = MailTools()
        self.admin_tools = AdminTools()
        self.cryption_tools = CryptionTools()

    def find_admin(self, email, password):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            req = (
                f"""SELECT `IDAdmin`, `Nom`, `Prenom`, `Mail`, `MDP`, `Role`, `Desactive`, `MarkedAsDeleted` FROM admin 
                WHERE Mail = "{email}" AND MDP = "{self.cryption_tools.crypt_sha256(password)}"  """)
            print(req)
            self.cursor.execute(req)
            data = self.cursor.fetchone()
            self.cursor.close()
            self.connection.close()
            if data is None:
                return 'failed', 'Admin not found'
            else:
                admin = Admin(data[0], data[1], data[2], data[3], 'None', data[5], data[6], data[7])
            return 'success', admin
        except Exception as e:
            return 'error', e

    def find_admin_by_id(self, id_utilisateur):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDAdmin`, `Nom`, `Prenom`, `Mail`, `MDP`, `Role`, `Desactive`, `MarkedAsDeleted` FROM admin 
                WHERE IDAdmin = '{id_utilisateur}'""")
            data = self.cursor.fetchone()
            self.cursor.close()
            self.connection.close()
            if data is None:
                return 'failed', 'Admin not found'
            else:
                admin = Admin(data[0], data[1], data[2], data[3], 'None', data[5], data[6], data[7])
            return 'success', admin.dict_form()
        except Exception as e:
            return 'error', e

    def change_details(self, id_admin, prenom, nom, email):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""UPDATE admin SET Nom = '{nom}', Prenom = '{prenom}', Mail = '{email}' 
                WHERE IDAdmin = {id_admin}""")
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            return 'success'
        except Exception as e:
            return 'error', e

    def find_all_admin(self):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDAdmin`, `Nom`, `Prenom`, `Mail`, `Role`, `Desactive`, `MarkedAsDeleted`
                 FROM admin WHERE Role <> 1 AND MarkedAsDeleted = -1""")
            data = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
            if data is None:
                return 'failed', 'Admin not found'
            else:
                admins = []
                for admin in data:
                    admins.append(
                        Admin(admin[0], admin[1], admin[2], admin[3], 'None', admin[4], admin[5], admin[6]).dict_form())
            return 'success', admins
        except Exception as e:
            return 'error', e

    def desactivate_admin(self, ida):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""UPDATE admin SET Desactive = 1 WHERE IDAdmin = {ida}""")
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            return 'success'
        except Exception as e:
            return 'error', e

    def activate_admin(self, ida):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""UPDATE admin SET Desactive = -1 WHERE IDAdmin = {ida}""")
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            return 'success'
        except Exception as e:
            return 'error', e

    def add_admin(self, nom, prenom, email, role):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""INSERT INTO admin (Nom, Prenom, Mail, MDP, Role, Desactive, MarkedAsDeleted) 
                VALUES ('{nom}', '{prenom}', '{email}', '', {role}, -1, -1)""")
            lid = self.cursor.lastrowid
            pwd, crypted = self.admin_tools.generate_admin_password(lid)
            self.mail_tools.send_admin_add_verification_mail(email, pwd)
            self.cursor.execute(
                f"""UPDATE admin SET MDP = '{crypted}' WHERE IDAdmin = {lid}""")
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            return 'success'
        except Exception as e:
            return 'error', e

    def delete_admin(self, ida):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""UPDATE admin SET MarkedAsDeleted = 1, Mail = NULL WHERE IDAdmin = {ida}""")
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            return 'success'
        except Exception as e:
            return 'error', e
