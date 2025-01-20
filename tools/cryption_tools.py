import hashlib


class CryptionTools:
    def __init__(self):
        ...

    def crypt_sha256(self, text):
        crypted_text = hashlib.sha256(text.encode()).hexdigest()
        return text
