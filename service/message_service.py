from entities.message import Message
from tools.database_tools import DatabaseConnection


class MessageService:
    def __init__(self):
        self.cursor = None
        self.connection = None
        self.database_tools = DatabaseConnection()

    def find_message_by_something(self, add):
        try:
            self.connection, self.cursor = self.database_tools.find_connection()
            self.cursor.execute(
                f"""SELECT `IDMessage`, `UtilisateurMessage`, `DateMessage`, `SujetMessage`, `ContenuMessage` 
                FROM message WHERE {add}""")
            data = self.cursor.fetchall()
            liste_message = []
            for element in data:
                message = Message(element[0], element[1], element[2], element[3], element[4])
                liste_message.append(message.dict_form())
            self.cursor.close()
            self.connection.close()
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
        Sujet, Contenu) VALUES ({utilisateur}, '{sujet}', '{contenu}')""")
