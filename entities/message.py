class Message:
    def __init__(self, id_message, utilisateur_message, date_message, sujet_message, contenu_message):
        self.id_message = id_message
        self.utilisateur_message = utilisateur_message
        self.date_message = date_message
        self.sujet_message = sujet_message
        self.contenu_message = contenu_message

    def dict_form(self):
        return {
            'id_message': self.id_message,
            'utilisateur_message': self.utilisateur_message,
            'date_message': self.date_message,
            'sujet_message': self.sujet_message,
            'contenu_message': self.contenu_message
        }


if __name__ == '__main__':
    pass
