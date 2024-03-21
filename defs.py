
from database import db_manager
import random
import string
import hashlib
from datetime import datetime


# Fonction pour générer un identifiant unique basé sur le prénom et le nom
def gen_id(prenom, nom):
    return prenom[0].lower() + nom.lower()


# Fonction pour créer un mot de passe fort aléatoirement
def mdp_fort():
    taille = random.randint(8, 12)  # Taille aléatoire entre 8 et 12 caractères
    caracteres = string.ascii_letters + string.digits + string.punctuation  # Ensemble de caractères possibles
    mdp = ''.join(random.choice(caracteres) for _ in range(taille))  # Génération du mot de passe
    return mdp


# Fonction pour hasher un mot de passe avec SHA-256
def hash_password(password):
    hasher = hashlib.sha256()  # Création de l'objet hasher
    hasher.update(password.encode('utf-8'))  # Hashage du mot de passe
    return hasher.hexdigest()  # Retour du mot de passe hashé


# Fonction pour demander la date d'embauche ou utiliser la date actuelle par défaut
def demander_date_embauche():
    date_embauche_str = input("Date d'embauche de l'employé (AAAA-MM-JJ) : ")
    return date_embauche_str or datetime.now().strftime('%Y-%m-%d')  # Retour de la date d'embauche


# Fonction pour enregistrer un employé dans la base de données
def enregistrer_employe(prenom, nom, email, numero, date_embauche):
    login = gen_id(prenom, nom)  # Génération de l'identifiant
    mdp = mdp_fort()
    mdp_hash = hash_password(mdp)  # Hashage du mot de passe
    mdp_creation_date = datetime.now().strftime('%Y-%m-%d')
    # Tentative d'insertion de l'employé dans la base de données
    success = db_manager.insert_employee(prenom, nom, login, mdp_hash, email, numero, date_embauche, mdp_creation_date)
    if success:
        return login, mdp  # Retour de l'identifiant et du mot de passe si succès
    else:
        print(f"Erreur: L'identifiant {login} ou l'email {email} existe déjà dans la base de données.")
        return None, None


# Fonction pour vérifier si un employé est présent dans la base de données
def verifier_employe_dans_db(login, mdp):
    mdp_hash = hashlib.sha256(mdp.encode('utf-8')).hexdigest()  # Hashage du mot de passe
    # Requête SQL pour trouver l'employé dans la base de données
    employe = db_manager.cursor.execute('''
        SELECT * FROM employes WHERE login = ? AND mdp = ?
    ''', (login, mdp_hash)).fetchone()
    return employe is not None  # Retourne True si l'employé est trouvé, sinon False
