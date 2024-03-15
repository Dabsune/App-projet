import hashlib
import random
import string
from datetime import datetime, timedelta


class Utilisateur:
    def __init__(self, prenom, nom, profil, droits):
        self.prenom = prenom
        self.nom = nom
        self.login = self.generer_login()
        self.password = self.generer_password()
        self.profil = profil
        self.droits = droits
        self.date_creation = datetime.now()

    def generer_login(self):
        return (self.prenom[0] + self.nom).lower()

    def generer_password(self, taille=12):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(taille))

    def modifier(self, prenom=None, nom=None, profil=None, droits=None):
        if prenom:
            self.prenom = prenom
        if nom:
            self.nom = nom
        if profil:
            self.profil = profil
        if droits:
            self.droits = droits

    def changer_password(self):
        self.password = self.generer_password()

    def supprimer(self):
        # Code pour supprimer l'utilisateur de la base de données
        pass


class GestionUtilisateurs:
    def __init__(self):
        self.utilisateurs = []

    def creer_utilisateur(self, prenom, nom, profil, droits):
        utilisateur = Utilisateur(prenom, nom, profil, droits)
        self.utilisateurs.append(utilisateur)

    def modifier_utilisateur(self, login, **kwargs):
        for utilisateur in self.utilisateurs:
            if utilisateur.login == login:
                utilisateur.modifier(**kwargs)
                break

    def supprimer_utilisateur(self, login):
        for utilisateur in self.utilisateurs:
            if utilisateur.login == login:
                self.utilisateurs.remove(utilisateur)
                utilisateur.supprimer()
                break
