import hashlib
from random import randint


class CryptionTools:
    def __init__(self):
        ...

    def crypt_sha256(self, text):
        crypted_text = hashlib.sha256(text.encode()).hexdigest()
        return crypted_text

    def generate_code_barre_utilisateur(self, code):
        ch = ''
        for i in code:
            if "A" <= i <= "Z" or "a" <= i <= "z":
                ch += str(ord(i))
            else:
                ch += str(i)
        while len(ch) < 11:
            ch = '0' + ch
        ch = '2' + ch
        print("code a barre : ", code, " => ", ch)
        return ch

    def generate_user_password(self, id_user):
        password = self.genrate_random_string(5) + str(id_user) + self.genrate_random_string(9)
        return password, self.crypt_sha256(password)

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
