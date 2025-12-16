import random              # Module permettant de faire des choix aléatoires

# LISTE DES MOTS POSSIBLES
# Tous les mots sont en MAJUSCULES pour simplifier les comparaisons
liste_mots = [
    "PYTHON", "ORDINATEUR", "PROGRAMME", "ALGORITHME", "MALADIE",
    "DOCTEUR", "INFIRMIER", "ETUDIANT", "JOUR", "RESEAU",
    "COMPORTEMENT", "EDUCATION", "MAISON", "INDICATION", "CHEMIN",
    "PAYS", "ORGANISATION", "ENCADREMENT", "ARGENT", "GARDIEN",
    "MAIRE", "CHAUFFEUR", "VOLEUR", "ROUTE", "TENUE", "JARDIN",
    "COPILOT", "DEEPSEEK", "MOTO", "DEVELOPPER", "SECRET",
    "NUIT", "CLOUD", "INFO"
]

# INITIALISATION DU JEU
# Choisit un mot au hasard dans la liste
mot_a_deviner = random.choice(liste_mots)

# Stocke la longueur du mot choisi
longueur_mot = len(mot_a_deviner)

print("   JEU DU PENDU    ")

# Crée une liste de "#" correspondant aux lettres cachées du mot
# Exemple : PYTHON → ['#', '#', '#', '#', '#', '#']
etat_mot = ["#" for _ in mot_a_deviner]

# Nombre maximum d'essais autorisés
nombre_essais = 6

# BOUCLE PRINCIPALE DU JEU (6 essais)
for essai in range(1, nombre_essais + 1):
    print("\nEssai", essai)

    # Demande une lettre à l'utilisateur et la convertit en majuscule
    lettre = input("Proposez une lettre : ").upper()

    # Vérifie si la lettre est contenue dans le mot à deviner
    if lettre in mot_a_deviner:

        # Parcourt chaque position du mot
        for i in range(longueur_mot):
            # Si la lettre correspond à une lettre du mot
            if mot_a_deviner[i] == lettre:
                # Remplace le # par la lettre trouvée
                etat_mot[i] = lettre

        # Affiche l'état actuel du mot avec des séparateurs
        affichage = "˽".join(etat_mot)
        print(affichage)

    else:
        # Si la lettre n'est pas dans le mot, on affiche l'état inchangé
        print("˽".join(etat_mot))

# PHASE FINALE : DEVINER LE MOT COMPLET

# Demande à l'utilisateur de proposer le mot entier
mot_final = input("\nProposez le mot complet : ").upper()

# Vérifie si le mot proposé est correct
if mot_final == mot_a_deviner:
    print("🎉 GAGNE 🎉")
else:
    print("❌ PERDU ❌")
    print("Le mot était :", mot_a_deviner)
