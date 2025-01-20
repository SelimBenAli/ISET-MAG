class Location:
    def __init__(self, id_location, date_debut_estimee, date_fin_estimee, utilisateur, hardware, admin,
                 quantite, confirmation, date_confirmation):
        self.id_location = id_location
        self.date_debut_estimee = date_debut_estimee
        self.date_fin_estimee = date_fin_estimee
        self.utilisateur = utilisateur
        self.hardware = hardware
        self.admin = admin
        self.quantite = quantite
        self.confirmation = confirmation
        self.date_confirmation = date_confirmation

    def dict_form(self):
        return {'id_location': self.id_location, 'date_debut_estimee': self.date_debut_estimee,
                'date_fin_estimee': self.date_fin_estimee, 'utilisateur': self.utilisateur, 'hardware': self.hardware,
                'admin': self.admin, 'quantite': self.quantite, 'confirmation': self.confirmation,
                'date_confirmation': self.date_confirmation}
