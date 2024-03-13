class Employee:
    def __init__(self, initIdentifiant, initNom, initPrenom, initEmail, initNumero, initCodeProjet):
        self.id = initIdentifiant
        self.nom = initNom
        self.prenom = initPrenom
        self.email = initEmail
        self.numero = initNumero
        self.codeprojet = initCodeProjet

class Admin (Employee):
    def __init__(self, initNom, initPrenom, initEmail, initNumero, initCodeProjet):
        super().__init__(initNom, initPrenom, initEmail, initNumero, initCodeProjet)

class SuperAdmin (Employee):
    def __init__(self)
