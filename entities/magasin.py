class Magasin:
    def __init__(self, id_magasin, nom_magasin, salle_magasin):
        self.id_magasin = id_magasin
        self.nom_magasin = nom_magasin
        self.salle_magasin = salle_magasin

    def dict_form(self):
        return {'id_magasin': self.id_magasin, 'nom_magasin': self.nom_magasin, 'salle_magasin': self.salle_magasin}
