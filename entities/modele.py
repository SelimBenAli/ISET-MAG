class Modele:
    def __init__(self, id_modele, nom_modele, marque):
        self.id_modele = id_modele
        self.nom_modele = nom_modele
        self.marque = marque

    def dict_form(self):
        return {'id_modele': self.id_modele, 'nom_modele': self.nom_modele, 'marque_modele': self.marque}
