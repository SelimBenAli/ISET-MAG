class Location:
    def __init__(self, id_location, date_debut_estimee, date_fin_estimee, utilisateur, modele, admin,
                 quantite, confirmation, date_confirmation):
        self.id_location = id_location
        self.date_debut_estimee = date_debut_estimee
        self.date_fin_estimee = date_fin_estimee
        self.utilisateur = utilisateur
        self.modele = modele
        self.admin = admin
        self.quantite = quantite
        self.confirmation = confirmation
        self.date_confirmation = date_confirmation

    def dict_form(self):
        return {'id_location': self.id_location, 'date_debut_estimee_location': self.date_debut_estimee,
                'date_fin_estimee_location': self.date_fin_estimee, 'utilisateur_location': self.utilisateur,
                'modele_location': self.modele,
                'admin_location': self.admin, 'quantite_location': self.quantite,
                'confirmation_location': self.confirmation,
                'date_confirmation_location': self.date_confirmation}
