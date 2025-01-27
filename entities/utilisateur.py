class Utilisateur:
    def __init__(self, id_utilisateur, nom_utilisateur, prenom_utilisateur, mail, telephone, mdp, code, role, compte):
        self.id_utilisateur = id_utilisateur
        self.nom_utilisateur = nom_utilisateur
        self.prenom_utilisateur = prenom_utilisateur
        self.mail = mail
        self.telephone = telephone
        self.role = role
        self.mdp = mdp
        self.code = code
        self.compte = self.convert_to_name(compte)

    @staticmethod
    def convert_to_name(compte):
        if compte == -1:
            return "Pas Encore Envoyé"
        if compte == 0:
            return "Pas Encore Confirmé"
        if compte == 1:
            return "Active"
        if compte == 2:
            return "Banni"

    def dict_form(self):
        return {'id_utilisateur': self.id_utilisateur, 'nom_utilisateur': self.nom_utilisateur,
                'prenom_utilisateur': self.prenom_utilisateur, 'mail_utilisateur': self.mail,
                'telephone_utilisateur': self.telephone, 'mdp_utilisateur': self.mdp,
                'role_utilisateur': self.role, 'code_utilisateur': self.code, "compte_utilisateur": self.compte}

    def reduced_dict_form(self):
        return {'id_utilisateur': self.id_utilisateur, 'nom_utilisateur': self.nom_utilisateur,
                'prenom_utilisateur': self.prenom_utilisateur, 'mail_utilisateur': self.mail,
                'telephone_utilisateur': self.telephone,
                'role_utilisateur': self.role, 'code_utilisateur': self.code, "compte_utilisateur": self.compte}
