class ConfigTools:
    def __init__(self):
        # ADMIN
        self.subject_admin = "Confirmation de rejoindre notre équipe ISETN - MAG"
        self.message_admin = """Félicitations, vous avez été ajouté à notre équipe ISETN - MAG.
         Vous pouvez maintenant accéder à votre compte en utilisant les informations suivantes:
         \n\nNom d'utilisateur: {email}\nMot de passe: {password}\n
         Vous pouvez accéder à dashboard admin à partir de ce lien : {link}\n\nCordialement,\nISETN - MAG"""

        # USER
        self.subject_user = "Confirmation de votre compte ISETN - MAG"
        self.message_user = """Félicitations, votre compte ISETN - MAG a été créé avec succès.
         Vous pouvez maintenant accéder à votre compte en utilisant les informations suivantes:
         \n\nNom d'utilisateur: {email}\nMot de passe: {password}\n
         Vous pouvez accéder à dashboard utilisateur à partir de ce lien : {link}\n\nCordialement,\nISETN - MAG"""

        # RECOVERY
        self.subject_recovery = "Récupération de votre compte ISET - MAG"
        self.message_recovery = """ Votre nouveau mot de passe est : {password} \n\n Cordialement,\nISETN - MAG"""
