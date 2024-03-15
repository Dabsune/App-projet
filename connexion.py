import generation

def verifier_identifiants(identifiant, mdp):
    # Vérifie si l'identifiant et le mot de passe correspondent à ceux enregistrés dans la base de données
    return generation.verifier_employe_dans_db(identifiant, mdp)

def demander_identifiants():
    for essai in range(5):
        identifiant_saisi = input("Entrez votre identifiant : ")
        mdp_saisi = input("Entrez votre mot de passe : ")
        if verifier_identifiants(identifiant_saisi, mdp_saisi):
            print("Accès autorisé.")
            return True
        else:
            print(f"Tentative {essai + 1}/5 échouée. Veuillez réessayer.")
    print("Accès refusé. Veuillez contacter l'administrateur.")
    return False

if __name__ == "__main__":
    demander_identifiants()
