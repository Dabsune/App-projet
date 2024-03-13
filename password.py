nom = input("Entrez un nom: ")
mdp = input("Entrez un mot de passe: ")
nbr = 5
while True:
    attempt = input("Mot de passe: ")
    if attempt != mdp:
        nbr = nbr - 1
        if nbr == 0:
            print("Compte bloqué")
            break
        else:
            print("Mot de passe erroné, veuillez réessayer (" + str(nbr), "essais restants)")
    else:
        print("Bienvenue,", nom)
        break
