import generation

# Demander les informations de l'employé et les enregistrer
prenom = input("Quel est le prénom de l'employé ? ")
nom = input("Quel est le nom de l'employé ? ")
identifiant, mdp = generation.enregistrer_employe(prenom, nom)
print(f"L'identifiant et le mot de passe de {prenom} {nom} ont été créés.\nId: {identifiant}\nMdp: {mdp}")
