class Etat:
    def __init__(self, id_etat, nom_etat, description):
        self.id_etat = id_etat
        self.nom_etat = nom_etat
        self.description = description
        
    def dict_form(self):
        return {'id_etat': self.id_etat, 'nom_etat': self.nom_etat, 'description_etat': self.description}
