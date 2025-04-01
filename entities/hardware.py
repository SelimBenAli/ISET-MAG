class Hardware:
    def __init__(self, id_hardware, modele, fournisseur, magasin, salle, etat, numero_inventaire, date_achat,
                 date_mise_service, date_ajout,
                 code_hardware, historique_relation):
        self.id_hardware = id_hardware
        self.modele = modele
        self.fournisseur = fournisseur
        self.magasin = magasin
        self.salle = salle
        self.etat = etat
        self.numero_inventaire = numero_inventaire
        self.date_achat = date_achat
        self.date_mise_service = date_mise_service
        self.date_ajout = date_ajout
        self.code_hardware = code_hardware
        self.historique_relation = historique_relation

    def dict_form(self):
        return {'id_hardware': self.id_hardware, 'modele_hardware': self.modele,
                'fournisseur_hardware': self.fournisseur,
                'magasin_hardware': self.magasin, 'salle_hardware': self.salle, 'etat_hardware': self.etat,
                'numero_inventaire_hardware': self.numero_inventaire, 'date_achat_hardware': self.date_achat,
                'date_mise_service_hardware': self.date_mise_service, 'date_ajout_hardware': self.date_ajout,
                'code_hardware': self.code_hardware, 'historique_relation_hardware': self.historique_relation}


if __name__ == '__main__':
    pass
