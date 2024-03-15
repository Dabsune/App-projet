import random
import string
import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('BDD.db')
cursor = conn.cursor()

# Création de la table des employés si elle n'existe pas déjà

cursor.execute('''
CREATE TABLE IF NOT EXISTS employes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nom TEXT,
    prenom TEXT,
    login TEXT UNIQUE,
    mdp TEXT,
    email TEXT UNIQUE,
    numero NUMERIC UNIQUE,
    embauche DATE
)
''')

# Création de la table unitée si elle n'existe pas déjà
cursor.execute('''
CREATE TABLE IF NOT EXISTS unitee (
    id_unitee INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    region TEXT,
    nb_employe NUMERIC,
    date_de_creation DATE
)
''')

# Création de la table des metiers si elle n'existe pas déjà

cursor.execute('''
CREATE TABLE IF NOT EXISTS metier (
    id_metier INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    id_collaborateur INTEGER,
    id_medecin INTEGER,
    id_scientifique INTEGER,
    id_commercial INTEGER,
    FOREIGN KEY(id_collaborateur) REFERENCES collaborateur(id_collaborateur),
    FOREIGN KEY(id_medecin) REFERENCES medecin(id_medecin),
    FOREIGN KEY(id_scientifique) REFERENCES scientifique(id_scientifique),
    FOREIGN KEY(id_commercial) REFERENCES commercial(id_commercial)
)
''')

# Création des tables scientifique, commercial, médecin, collaborateur

cursor.execute('''
CREATE TABLE IF NOT EXISTS scientifique (
    id_scientifique INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    code_projet NUMERIC UNIQUE,
    nvAcces TEXT,
    nb_unite NUMERIC
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS commercial (
    id_commercial INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nvAcces TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS medecin (
    id_medecin INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nvAcces TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS collaborateur (
    id_collaborateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nvAcces TEXT
)
''')

conn.commit()

def gen_id(prenom, nom):
    # Crée un login à partir du prénom+nom
    return prenom[0].lower() + nom.lower()


def mdp_fort(taille=8):
    # Génère un mot de passe aléatoire avec ces 4 critères
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mdp = [random.choice(set) for set in
           (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)]
    mdp += random.choices(caracteres, k=taille - 4)
    random.shuffle(mdp)
    return ''.join(mdp)


def enregistrer_employe(prenom, nom):
    login = gen_id(prenom, nom)
    mdp = mdp_fort(taille=10)
    try:
        # Insertion des données dans la base de données SQLite
        cursor.execute('INSERT INTO employes (prenom, nom, login, mdp) VALUES (?, ?, ?, ?)',
                       (prenom, nom, login, mdp))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Erreur: L'identifiant {login} existe déjà dans la base de données.")
        return None, None
    return login, mdp


def verifier_employe_dans_db(login, mdp):
    # Vérifie si l'employé avec l'login donné existe dans la base de données
    cursor.execute('SELECT mdp FROM employes WHERE login = ?', (login,))
    mdp_enregistre = cursor.fetchone()
    return mdp_enregistre is not None and mdp_enregistre[0] == mdp

# Assurez-vous de fermer la connexion à la base de données lorsque vous avez terminé
# conn.close()
