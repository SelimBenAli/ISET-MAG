class Role:
    def __init__(self, id_role, nom_role):
        self.id_role = id_role
        self.nom_role = nom_role

    def dict_form(self):
        return {'id_role': self.id_role, 'nom_role': self.nom_role}


if __name__ == '__main__':
    pass
