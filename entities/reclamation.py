class Reclamation:
    def __init__(self, id_reclamation, hardware, utilisateur, intervention, etat, description,
                 date_reclamation):
        self.id_reclamation = id_reclamation
        self.hardware = hardware
        self.utilisateur = utilisateur
        self.intervention = intervention
        self.etat = etat
        self.description = description
        self.date_reclamation = date_reclamation

    def dict_form(self):
        return {'id_reclamation': self.id_reclamation, 'hardware': self.hardware, 'utilisateur': self.utilisateur,
                'intervention': self.intervention, 'etat': self.etat, 'description': self.description,
                'date_reclamation': self.date_reclamation}
