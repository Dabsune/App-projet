import random
import string

# Dictionnaire pour stocker les noms et le mot de passe correspondant
employes = {}

prenom = input("Quel est le prénom de l'employé ? ")
nom = input("Quel est le nom de l'employé ? ")


def gen_id(prenom, nom):
    # Crée un identifiant à partir du prénom+nom
    identifiant = prenom[0].lower() + nom.lower()
    return identifiant


def mdp_fort(taille=8):
    # Génère un mot de passe aléatoire avec ces 4 critères
    min = string.ascii_lowercase
    maj = string.ascii_uppercase
    nbr = string.digits
    sym = string.punctuation

    # Initialise le mot de passe avec un caractère de chaque type pour respecter les critères
    mdp = [random.choice(min), random.choice(maj), random.choice(nbr), random.choice(sym)]

    # Complète le reste du mot de passe jusqu'à la taille souhaitée
    if taille > 4:
        mdp += random.choices(min + maj + nbr + sym, k=taille - 4)

    random.shuffle(mdp)  # Mélange les caractères
    mdp_final = ''.join(mdp)
    return mdp_final


# Génération de l'identifiant
identifiant = gen_id(prenom, nom)

# Génération du mot de passe
mdp_final = mdp_fort(taille=10)

# Enregistrement dans le dictionnaire
employes[identifiant] = mdp_final

print(f"Le nouveau mot de passe de \"{identifiant}\" est : {mdp_final}")
