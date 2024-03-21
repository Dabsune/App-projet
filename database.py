import sqlite3

DB_PATH = 'BDD.db'


# Classe pour gérer la connexion à la base de données et les opérations associées
class Database:
    # Initialisation de la classe avec la base de données spécifiée
    def __init__(self, base_de_donnees):
        self.conn = sqlite3.connect(base_de_donnees)  # Connexion à la base de données
        self.cursor = self.conn.cursor()  # Création d'un curseur pour exécuter des requêtes SQL
        self.setup_tables()  # Configuration des tables

    # Méthode pour configurer les tables de la base de données
    def setup_tables(self):
        # Création des tables si elles n'existent pas déjà
        pass

    # Méthode pour insérer un nouvel employé dans la base de données
    def insert_employee(self, prenom, nom, login, mdp, email, numero, date_embauche, mdp_creation_date):
        try:
            # Exécution de la requête SQL pour insérer un nouvel employé
            self.cursor.execute('''
                INSERT INTO employes (prenom, nom, login, mdp, email, numero, embauche, mdp_creation_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (prenom, nom, login, mdp, email or None, numero or None, date_embauche, mdp_creation_date))
            self.conn.commit()  # Validation des modifications dans la base de données
            return True
        except sqlite3.IntegrityError as e:
            # Gestion des erreurs d'intégrité, par exemple si un employé existe déjà
            print(f"Erreur d'intégrité : {e}")
            return False

    def close(self):
        self.conn.close()  # Fermeture de la connexion


# Instanciation de la base de données avec le chemin spécifié
db_manager = Database(DB_PATH)
