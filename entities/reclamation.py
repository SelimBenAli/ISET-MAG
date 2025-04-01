class Reclamation:
    def __init__(self, id_reclamation, hardware, utilisateur, intervention, etat, description,
                 date_reclamation, vu, technicien, description_technicien, date_technicien_reclamation):
        self.id_reclamation = id_reclamation
        self.hardware = hardware
        self.utilisateur = utilisateur
        self.intervention = intervention
        self.etat = etat
        self.description = description
        self.date_reclamation = date_reclamation
        self.vu = vu
        self.technicien = technicien
        self.description_technicien = description_technicien
        self.date_technicien_reclamation = date_technicien_reclamation

    def dict_form(self):
        return {'id_reclamation': self.id_reclamation, 'hardware_reclamation': self.hardware,
                'utilisateur_reclamation': self.utilisateur,
                'intervention_reclamation': self.intervention, 'etat_reclamation': self.etat,
                'description_reclamation': self.description,
                'date_reclamation': self.date_reclamation, 'vu_reclamation': self.vu,
                'technicien_reclamation': self.technicien,
                'description_technicien_reclamation': self.description_technicien,
                'date_technicien_reclamation': self.date_technicien_reclamation}


if __name__ == '__main__':
    pass
