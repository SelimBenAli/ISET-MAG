class Bloc:
    def __init__(self, id_bloc, nom_bloc):
        self.id_bloc = id_bloc
        self.nom_bloc = nom_bloc

    def dict_form(self):
        return {'id_bloc': self.id_bloc, 'nom_bloc': self.nom_bloc}


if __name__ == '__main__':
    pass
