from entities.parametre_email import ParametreEmail
from tools.cryption_tools import CryptionTools
from tools.database_tools import DatabaseConnection
from tools.mail_tools import MailTools


class ParametreEmailService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()
        self.cryption_tools = CryptionTools()
        self.mail_tools = MailTools()

    # EMAIL PARAMETER IDs :
    # 1 : Admin add email
    # 2 : User add email
    # 3 : User forgot password email

    def find_marametre_add_admin_email(self):
        self.find_parametre_email_by_id(1)

    def find_marametre_add_user_email(self):
        self.find_parametre_email_by_id(2)

    def find_marametre_forgot_password_email(self):
        self.find_parametre_email_by_id(3)

    def find_parametre_email_by_id(self, id_parametre_email):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            req = (
                f"""SELECT IDParametre, Nom, objet, `Text`
                 FROM parametre_email WHERE IDParametre = {id_parametre_email}""")
            self.cursor.execute(req)
            data = self.cursor.fetchall()
            liste_parametre_email = []
            for element in data:
                parametre_email = ParametreEmail(element[0], element[1], element[2], element[3])
                liste_parametre_email.append(parametre_email.dict_form())
            try:
                self.cursor.close()
                self.connection.close()
            except Exception as e:
                ...
            return 'success', liste_parametre_email
        except Exception as e:
            return 'error', e

    def find_all_parametre_email(self):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            req = (f"""SELECT IDParametre, Nom, objet, `Text`
                      FROM parametre_email""")
            self.cursor.execute(req)
            data = self.cursor.fetchall()
            liste_parametre_email = []
            for element in data:
                parametre_email = ParametreEmail(element[0], element[1], element[2], element[3])
                liste_parametre_email.append(parametre_email.dict_form())
            try:
                self.cursor.close()
                self.connection.close()
            except Exception as e:
                ...
            return 'success', liste_parametre_email
        except Exception as e:
            return 'error', e


    def update_parametre_email(self, id_parametre_email, nom, objet, text):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            req = (f"""UPDATE parametre_email SET Nom = '{nom}', objet = '{objet}', `Text` = '{text}'
                      WHERE IDParametre = {id_parametre_email}""")
            self.cursor.execute(req)
            self.connection.commit()
            try:
                self.cursor.close()
                self.connection.close()
            except Exception as e:
                ...
            return 'success', None
        except Exception as e:
            return 'error', e


if __name__ == '__main__':
    pass
