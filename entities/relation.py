class Relation:
    def __init__(self, id_relation, hardware_1, hardware_2):
        self.id_relation = id_relation
        self.hardware_1 = hardware_1
        self.hardware_2 = hardware_2

    def dict_form(self):
        return {'id_relation': self.id_relation, 'hardware_1': self.hardware_1, 'hardware_2': self.hardware_2}


if __name__ == '__main__':
    pass
