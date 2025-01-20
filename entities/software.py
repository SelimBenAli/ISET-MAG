class Software:
    def __init__(self, id_software, nom_software, date_achat, date_ajout, lien):
        self.id_software = id_software
        self.nom_software = nom_software
        self.date_achat = date_achat
        self.date_ajout = date_ajout
        self.lien = lien

    def dict_form(self):
        return {'id_software': self.id_software, 'nom_software': self.nom_software, 'date_achat': self.date_achat,
                'date_ajout': self.date_ajout, 'lien': self.lien}
