class Admin:
    def __init__(self, id_admin, nom_admin, prenom_admin, email_admin, password_admin, role_admin, descative,
                 marked_as_deleted):
        self.id_admin = id_admin
        self.nom_admin = nom_admin
        self.prenom_admin = prenom_admin
        self.email_admin = email_admin
        self.password_admin = password_admin
        self.role_admin = role_admin
        self.descative = descative
        self.marked_as_deleted = marked_as_deleted

    def dict_form(self):
        return {'id_admin': self.id_admin, 'nom_admin': self.nom_admin, 'prenom_admin': self.prenom_admin,
                'email_admin': self.email_admin, 'role_admin': self.role_admin, 'desactive_admin': self.descative,
                'marked_as_deleted': self.marked_as_deleted}
