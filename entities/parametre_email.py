class ParametreEmail:
    def __init__(self, id_parametre_email, nom_parametre_email, objet_parametre_email, message_parametre_email):
        self.id_parametre_email = id_parametre_email
        self.nom_parametre_email = nom_parametre_email
        self.objet_parametre_email = objet_parametre_email
        self.message_parametre_email = message_parametre_email

    def dict_form(self):
        return {'id_parametre_email': self.id_parametre_email, 'nom_parametre_email': self.nom_parametre_email,
                'objet_parametre_email': self.objet_parametre_email,
                'message_parametre_email': self.message_parametre_email}


if __name__ == '__main__':
    pass
