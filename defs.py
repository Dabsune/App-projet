import random
import string
import hashlib
from database import Database
from datetime import datetime

DB_PATH = 'BDD.db'
db_manager = Database(DB_PATH)


def gen_id(prenom, nom):
    return prenom[0].lower() + nom.lower()


def mdp_fort():
    taille = random.randint(8, 12)  # Taille aléatoire entre 8 et 12
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mdp = ''.join(random.choice(caracteres) for _ in range(taille))
    return mdp


def hash_password(password):
    hasher = hashlib.sha256()
    hasher.update(password.encode('utf-8'))
    return hasher.hexdigest()


def demander_date_embauche():
    date_embauche_str = input(
        "\n(Entrée => utiliser la date d'aujourd'hui) [Format AAAA-MM-JJ]\nDate d'embauche de l'employé : ")
    return date_embauche_str or datetime.now().strftime('%Y-%m-%d')


def enregistrer_employe(prenom, nom, email, numero, date_embauche):
    login = gen_id(prenom, nom)
    mdp = mdp_fort()
    mdp_hash = hash_password(mdp)
    mdp_creation_date = datetime.now().strftime('%Y-%m-%d')
    success = db_manager.insert_employee(prenom, nom, login, mdp_hash, email, numero, date_embauche, mdp_creation_date)
    if success:
        return login, mdp
    else:
        print(f"Erreur: L'identifiant {login} ou l'email {email} existe déjà dans la base de données.")
        return None, None


def get_password_age(login):
    employe = db_manager.cursor.execute('''
        SELECT mdp_creation_date FROM employes WHERE login = ?
    ''', (login,)).fetchone()
    if employe and employe[0]:
        mdp_creation_date = datetime.strptime(employe[0], '%Y-%m-%d')
        return (datetime.now() - mdp_creation_date).days
    return None


def change_password_by_admin(login, new_password):
    new_password_hash = hash_password(new_password)
    new_password_creation_date = datetime.now().strftime('%Y-%m-%d')
    db_manager.cursor.execute('''
        UPDATE employes SET mdp = ?, mdp_creation_date = ? WHERE login = ?
    ''', (new_password_hash, new_password_creation_date, login))
    db_manager.conn.commit()


def verifier_employe_dans_db(login, mdp):
    mdp_hash = hash_password(mdp)
    employe = db_manager.cursor.execute('''
        SELECT * FROM employes WHERE login = ? AND mdp = ?
    ''', (login, mdp_hash)).fetchone()
    return employe is not None


def is_admin(login):
    # Cette fonction vérifie si l'utilisateur avec le login donné est un admin
    employe = db_manager.cursor.execute('''
        SELECT is_admin FROM employes WHERE login = ?
    ''', (login,)).fetchone()
    return employe and employe[0]


def modify_employee(login, prenom=None, nom=None, email=None, numero=None, date_embauche=None):
    # Permettre à un admin de modifier les détails d'un employé
    if not is_admin(login):
        print("Vous n'avez pas les droits d'administrateur pour modifier les données.")
        return False

    # Construire la requête de mise à jour dynamiquement en fonction des arguments fournis
    fields_to_update = []
    values = []
    if prenom:
        fields_to_update.append("prenom = ?")
        values.append(prenom)
    if nom:
        fields_to_update.append("nom = ?")
        values.append(nom)
    if email:
        fields_to_update.append("email = ?")
        values.append(email)
    if numero:
        fields_to_update.append("numero = ?")
        values.append(numero)
    if date_embauche:
        fields_to_update.append("embauche = ?")
        values.append(date_embauche)

    if not fields_to_update:
        print("Aucune donnée fournie pour la mise à jour.")
        return False

    update_query = "UPDATE employes SET " + ", ".join(fields_to_update) + " WHERE login = ?"
    values.append(login)

    try:
        db_manager.cursor.execute(update_query, values)
        db_manager.conn.commit()
        print("Les données de l'employé ont été mises à jour avec succès.")
        return True
    except sqlite3.Error as e:
        print(f"Erreur lors de la mise à jour des données de l'employé : {e}")
        return False


def delete_employee(login):
    # Cette fonction permet à un admin de supprimer un employé
    if not is_admin(login):
        print("Vous n'avez pas les droits d'administrateur pour supprimer les données.")
        return False

    try:
        db_manager.cursor.execute('''
            DELETE FROM employes WHERE login = ?
        ''', (login,))
        db_manager.conn.commit()
        print("L'employé a été supprimé avec succès.")
        return True
    except sqlite3.Error as e:
        print(f"Erreur lors de la suppression de l'employé : {e}")
        return False
