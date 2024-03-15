
import sqlite3

DB_PATH = 'BDD.db'


class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        # Création des tables si elles n'existent pas déjà
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
        CREATE TABLE IF NOT EXISTS unite (
            id_unitee INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            region TEXT,
            nb_employe NUMERIC,
            date_de_creation DATE
        )
        ''')

        self.cursor.execute('''
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

    def insert_employee(self, prenom, nom, login, mdp, email, numero, date_embauche, mdp_creation_date):
        try:
            self.cursor.execute('''
                INSERT INTO employes (prenom, nom, login, mdp, email, numero, embauche, mdp_creation_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (prenom, nom, login, mdp, email or None, numero or None, date_embauche, mdp_creation_date))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Erreur d'intégrité : {e}")
            return False

    def close(self):
        self.conn.close()
