class Intervention:
    def __init__(self, id_intervention, utilisateur, salle, hardware, admin, date_debut, date_fin):
        self.id_intervention = id_intervention
        self.utilisateur = utilisateur
        self.salle = salle
        self.hardware = hardware
        self.admin = admin
        self.date_debut = date_debut
        self.date_fin = date_fin

    def dict_form(self):
        return {'id_intervention': self.id_intervention, 'utilisateur_intervention': self.utilisateur,
                'salle_intervention': self.salle,
                'hardware_intervention': self.hardware, 'admin_intervention': self.admin,
                'date_debut_intervention': self.date_debut,
                'date_fin_intervention': self.date_fin}
