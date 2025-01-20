class Marque:
    def __init__(self, id_marque, nom_marque):
        self.id_marque = id_marque
        self.nom_marque = nom_marque

    def dict_form(self):
        return {'id_marque': self.id_marque, 'nom_marque': self.nom_marque}
