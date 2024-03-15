import generation

# Demander les informations de l'employé et les enregistrer
prenom = input("Quel est le prénom de l'employé ? ")
nom = input("Quel est le nom de l'employé ? ")
login, mdp = generation.enregistrer_employe(prenom, nom)

if login and mdp:
    print(f"L'login et le mot de passe de {prenom} {nom} ont été créés et enregistrés dans la base de "
          f"données.\nId: {login}\nMdp: {mdp}")
else:
    print("L'enregistrement de l'employé a échoué.")
