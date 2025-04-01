from entities.message import Message
from service.utilisateur_service import UtilisateurService
from tools.database_tools import DatabaseConnection
from tools.date_tools import DateTools


class MessageService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()
        self.user_service = UtilisateurService()
        self.date_tools = DateTools()

    def find_message_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDMessage`, `IDUtilisateur`, `Date`, `Sujet`, `Contenu`
                FROM message WHERE {add}""")
            data = self.cursor.fetchall()
            liste_message = []
            for element in data:
                status, user = self.user_service.find_utilisateur_by_id(element[1])
                message = Message(element[0], user[0], self.date_tools.convert_date_time(element[2]), element[3],
                                  element[4])
                liste_message.append(message.dict_form())
            try:
                self.cursor.close()
                self.connection.close()
            except Exception as e:
                ...
            return 'success', liste_message
        except Exception as e:
            return 'error', e

    def find_all_message(self):
        return self.find_message_by_something(' 1')

    def find_message_by_id(self, id_message):
        return self.find_message_by_something(f' IDMessage = {id_message}')

    def find_message_by_utilisateur(self, utilisateur):
        return self.find_message_by_something(f" IDUtilisateur = {utilisateur}")

    def find_message_by_sujet(self, sujet):
        return self.find_message_by_something(f" Sujet LIKE '%{sujet}%'")

    def add_message(self, utilisateur, sujet, contenu):
        return self.database_tools.execute_request(f"""INSERT INTO message (IDUtilisateur, 
        Sujet, Contenu, Vu) VALUES ({utilisateur}, '{sujet}', '{contenu}', '')""")

    def delete_message(self, id_message):
        return self.database_tools.execute_request(f"""DELETE FROM message WHERE IDMessage = {id_message}""")

    def add_seen_message(self, id_message, id_utilisateur):
        self.connection, self.cursor = self.database_tools.find_connection()
        self.cursor.execute(f"""SELECT `Vu` FROM message WHERE IDMessage = {id_message}""")
        liste_vu = self.cursor.fetchone()
        my_list = ""
        if liste_vu is not None and liste_vu != "":
            liste_vu = liste_vu[0]
            my_list = liste_vu + f"{id_utilisateur};"
        return self.database_tools.execute_request(
            f"""UPDATE message SET Vu = '{my_list}' WHERE IDMessage = {id_message}""")

    def add_seen_all_message(self, id_utilisateur):
        self.connection, self.cursor = self.database_tools.find_connection()
        self.cursor.execute(f"""SELECT `IDMessage`, `Vu` FROM message WHERE `Vu` NOT LIKE "%{id_utilisateur}%;" """)
        liste_vues = self.cursor.fetchall()

        for liste_vu in liste_vues:

            if liste_vu is not None:
                vues = liste_vu[1]
                id_message = liste_vu[0]
                if vues is not None and vues != "":
                    my_list = str(vues) + f"{str(id_utilisateur)};"
                else:
                    my_list = f"{id_utilisateur};"
                req = (
                    f"""UPDATE message SET Vu = '{my_list}' WHERE IDMessage = {id_message}""")

                self.database_tools.execute_request(req)
        self.connection.commit()

        self.cursor.close()
        self.connection.close()

    def return_list_seen(self, id_message):
        self.connection, self.cursor = self.database_tools.find_connection()
        self.cursor.execute(f"""SELECT `Vu` FROM message WHERE IDMessage = {id_message}""")
        liste_vu = self.cursor.fetchone()
        if liste_vu is not None:
            liste_vu = liste_vu[0]
            return liste_vu.split(';')
        return []


if __name__ == '__main__':
    pass
