
from defs import demander_date_embauche, enregistrer_employe


def main():
    # Boucle infinie pour obtenir les informations de l'employé
    while True:
        prenom = input("Prénom de l'employé : ").strip()
        nom = input("Nom de l'employé : ").strip()
        email = input("Email de l'employé : ").strip()
        numero = input("Numéro de l'employé : ").strip()
        role = input("Rôle de l'employé : ").strip()
        region = input("Ville de l'employé : ").strip()

        # Vérification que le prénom et le nom ne sont pas vides
        if not prenom or not nom:
            print("Le prénom et le nom ne peuvent pas être laissés vides.\n")
        else:
            # Sortie de la boucle si les informations sont valides
            break

    # Appel de la fonction pour demander la date d'embauche
    date_embauche = demander_date_embauche()

    # Enregistrement de l'employé et récupération de l'identifiant et du mot de passe
    identifiant, mdp = enregistrer_employe(prenom, nom, email, numero, date_embauche)

    # Vérification de la réussite de l'enregistrement
    if identifiant and mdp:
        print(f"L'identifiant & le mot de passe de {prenom} {nom} ont été créés et enregistrés dans la base de données."
              f"\nId: {identifiant}\nMdp: {mdp}")
    else:
        # Message d'erreur si l'enregistrement échoue
        print("L'enregistrement de l'employé a échoué.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()
