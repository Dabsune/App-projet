
import defs

DB_PATH = 'BDD.db'


def main():
    while True:
        prenom = input("Prénom de l'employé : ").strip()
        nom = input("Nom de l'employé : ").strip()
        if not prenom or not nom:
            print("Le prénom et le nom ne peuvent pas être laissés vides.\n")
        else:
            break
    email = input("\n(Entrée => laisser vide)\nAdresse e-mail de l'employé : ")
    numero = input("\n(Entrée => laisser vide)\nNuméro de téléphone de l'employé : ")
    date_embauche = defs.demander_date_embauche()

    login, mdp = defs.enregistrer_employe(prenom, nom, email, numero, date_embauche)

    if login and mdp:
        print(f"L'identifiant & le mot de passe de {prenom} {nom} ont été créés et enregistrés."
              f"\nId: {login}\nMdp: {mdp}")
    else:
        print("L'enregistrement de l'employé a échoué.")


if __name__ == "__main__":
    main()
