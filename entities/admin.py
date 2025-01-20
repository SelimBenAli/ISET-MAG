class Admin:
    def __init__(self, id_admin, nom_admin, prenom_admin, email_admin, password_admin):
        self.id_admin = id_admin
        self.nom_admin = nom_admin
        self.prenom_admin = prenom_admin
        self.email_admin = email_admin
        self.password_admin = password_admin

    def dict_form(self):
        return {'id_admin': self.id_admin, 'nom_admin': self.nom_admin, 'prenom_admin': self.prenom_admin,
                'email_admin': self.email_admin}
