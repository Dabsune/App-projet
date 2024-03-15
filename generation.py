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
    prenom TEXT,
    nom TEXT,
    identifiant TEXT UNIQUE,
    mdp TEXT
)
''')
conn.commit()

def gen_id(prenom, nom):
    # Crée un identifiant à partir du prénom+nom
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
    identifiant = gen_id(prenom, nom)
    mdp = mdp_fort(taille=10)
    # Insertion des données dans la base de données SQLite
    cursor.execute('INSERT INTO employes (prenom, nom, identifiant, mdp) VALUES (?, ?, ?, ?)',
                   (prenom, nom, identifiant, mdp))
    conn.commit()
    return identifiant, mdp

def verifier_employe_dans_db(identifiant, mdp):
    # Vérifie si l'employé avec l'identifiant donné existe dans la base de données
    cursor.execute('SELECT mdp FROM employes WHERE identifiant = ?', (identifiant,))
    mdp_enregistre = cursor.fetchone()
    return mdp_enregistre is not None and mdp_enregistre[0] == mdp

# Assurez-vous de fermer la connexion à la base de données lorsque vous avez terminé
# conn.close()
