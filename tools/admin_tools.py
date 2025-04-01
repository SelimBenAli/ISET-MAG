from tools.database_tools import DatabaseConnection
from tools.cryption_tools import CryptionTools
from random import randint


class AdminTools:
    def __init__(self):
        self.database_tools = DatabaseConnection()
        self.cryption_tools = CryptionTools()

    def generate_admin_password(self, id_admin):
        password = self.genrate_random_string(5) + str(id_admin) + self.genrate_random_string(9)
        return password, self.cryption_tools.crypt_sha256(password)

    @staticmethod
    def genrate_random_string(length):
        string = ''
        for i in range(0, length):
            choix = randint(0, 2)
            if choix == 0:
                string += chr(randint(65, 90))
            elif choix == 1:
                string += chr(randint(97, 122))
            else:
                string += chr(randint(48, 57))
        return string


if __name__ == '__main__':
    admin_tools = AdminTools()

