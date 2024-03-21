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
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS employes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nom TEXT,
            prenom TEXT NOT NULL,
            login TEXT UNIQUE,
            mdp TEXT,
            email TEXT UNIQUE,
            numero NUMERIC UNIQUE,
            embauche DATE,
            mdp_creation_date DATE
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS scientifique (
            id_scientifique INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            code_projet NUMERIC UNIQUE,
            nvAcces TEXT,
            nb_unite NUMERIC
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS commercial (
            id_commercial INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nvAcces TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS medecin (
            id_medecin INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nvAcces TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS collaborateur (
            id_collaborateur INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nvAcces TEXT
        )
        ''')
        self.conn.commit()

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

    # Méthode pour supprimer un employé de la base de données
    def delete_employee(self, employee_id):
        try:
            self.cursor.execute('''
                DELETE FROM employes WHERE ID = ?
            ''', (employee_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erreur lors de la suppression de l'employé : {e}")
            return False

    # Méthode pour mettre à jour les informations d'un employé
    def update_employee(self, employee_id, prenom=None, nom=None, login=None, mdp=None, email=None, numero=None,
                        embauche=None, mdp_creation_date=None):
        try:
            # Préparation de la requête SQL avec les champs à mettre à jour
            fields = []
            values = []
            if prenom is not None:
                fields.append("prenom = ?")
                values.append(prenom)
            if nom is not None:
                fields.append("nom = ?")
                values.append(nom)
            if login is not None:
                fields.append("login = ?")
                values.append(login)
            if mdp is not None:
                fields.append("mdp = ?")
                values.append(mdp)
            if email is not None:
                fields.append("email = ?")
                values.append(email)
            if numero is not None:
                fields.append("numero = ?")
                values.append(numero)
            if embauche is not None:
                fields.append("embauche = ?")
                values.append(embauche)
            if mdp_creation_date is not None:
                fields.append("mdp_creation_date = ?")
                values.append(mdp_creation_date)

            # Construction de la requête SQL
            sql = f"UPDATE employes SET {', '.join(fields)} WHERE ID = ?"
            values.append(employee_id)

            # Exécution de la requête SQL
            self.cursor.execute(sql, values)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erreur lors de la mise à jour de l'employé : {e}")
            return False

    def close(self):
        self.conn.close()  # Fermeture de la connexion


# Instanciation de la base de données avec le chemin spécifié
db_manager = Database(DB_PATH)
