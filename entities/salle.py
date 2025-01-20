class Salle:
    def __init__(self, id_salle, nom_salle, bloc):
        self.id_salle = id_salle
        self.nom_salle = nom_salle
        self.bloc = bloc

    def dict_form(self):
        return {'id_salle': self.id_salle, 'nom_salle': self.nom_salle, 'bloc_salle': self.bloc}
