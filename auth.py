from defs import verifier_employe_dans_db


# Fonction qui vérifie les identifiants en utilisant la fonction importée
def verifier_identifiants(login, mdp):
    return verifier_employe_dans_db(login, mdp)


# Fonction qui demande à l'utilisateur de saisir ses identifiants jusqu'à 5 fois
def demander_identifiants():
    for essai in range(5):
        identifiant_saisi = input("Entrez votre identifiant : ")
        mdp_saisi = input("Entrez votre mot de passe : ")
        if verifier_identifiants(identifiant_saisi, mdp_saisi):  # Vérification des identifiants
            print("Accès autorisé.")
            return True
        else:
            # Message d'erreur si les identifiants sont incorrects
            print(f"Tentative {essai + 1}/5 échouée. Veuillez réessayer.")
    # Message d'erreur après 5 tentatives infructueuses
    print("Accès refusé. Veuillez contacter l'administrateur.")
    return False


# Point d'entrée du programme
if __name__ == "__main__":
    demander_identifiants()  # Appel de la fonction de demande d'identifiants
