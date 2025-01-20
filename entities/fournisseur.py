class Fournisseur:
    def __init__(self, id_fournisseur, nom_fournisseur, telephone_fournisseur):
        self.id_fournisseur = id_fournisseur
        self.nom_fournisseur = nom_fournisseur
        self.telephone_fournisseur = telephone_fournisseur

    def dict_form(self):
        return {'id_fournisseur': self.id_fournisseur, 'nom_fournisseur': self.nom_fournisseur,
                'telephone_fournisseur': self.telephone_fournisseur}
