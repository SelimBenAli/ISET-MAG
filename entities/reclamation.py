class Reclamation:
    def __init__(self, id_reclamation, hardware, utilisateur, intervention, etat, description,
                 date_reclamation, vu):
        self.id_reclamation = id_reclamation
        self.hardware = hardware
        self.utilisateur = utilisateur
        self.intervention = intervention
        self.etat = etat
        self.description = description
        self.date_reclamation = date_reclamation
        self.vu = vu

    def dict_form(self):
        return {'id_reclamation': self.id_reclamation, 'hardware_reclamation': self.hardware,
                'utilisateur_reclamation': self.utilisateur,
                'intervention_reclamation': self.intervention, 'etat_reclamation': self.etat,
                'description_reclamation': self.description,
                'date_reclamation': self.date_reclamation, 'vu_reclamation': self.vu}
