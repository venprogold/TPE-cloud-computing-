# FONCTION : encoder
# Rôle : chiffrer un texte en utilisant le chiffrement de César
# Principe : chaque lettre est décalée de +3 positions dans l’alphabet
# Exemple : A → D, X → A
# Les caractères non alphabétiques ne sont pas modifié
def encoder(nom):
    resultat = ""  # Chaîne qui contiendra le texte encodé final

    # Parcours de chaque caractère du texte entré par l'utilisateur
    for caractere in nom:

        # Vérifie si le caractère est une lettre majuscule (A à Z)
        if 'A' <= caractere <= 'Z':
            # Conversion du caractère en code ASCII (ord)
            # Décalage de +3 avec retour circulaire grâce au modulo 26
            resultat += chr((ord(caractere) - ord('A') + 3) % 26 + ord('A'))

        # Vérifie si le caractère est une lettre minuscule (a à z)
        elif 'a' <= caractere <= 'z':
            # Même principe que pour les majuscules
            resultat += chr((ord(caractere) - ord('a') + 3) % 26 + ord('a'))

        # Si le caractère n'est pas une lettre (espace, chiffre, symbole)
        else:
            # On le conserve tel quel
            resultat += caractere

    # Retourne le texte complètement encodé
    return resultat


# FONCTION : decoder
# Rôle : déchiffrer un texte encodé avec le décalage de César
# Principe : chaque lettre est décalée de -3 positions
# Exemple : D → A, A → X
def decoder(nom_code):
    resultat = ""  # Chaîne qui contiendra le texte décodé

    # Parcours de chaque caractère du texte encodé
    for caractere in nom_code:

        # Vérifie si le caractère est une lettre majuscule
        if 'A' <= caractere <= 'Z':
            # Décalage inverse (-3) avec gestion du retour alphabétique
            resultat += chr((ord(caractere) - ord('A') - 3) % 26 + ord('A'))

        # Vérifie si le caractère est une lettre minuscule
        elif 'a' <= caractere <= 'z':
            resultat += chr((ord(caractere) - ord('a') - 3) % 26 + ord('a'))

        # Les autres caractères restent inchangés
        else:
            resultat += caractere

    # Retourne le texte décodé
    return resultat


# PROGRAMME PRINCIPAL
# Affiche un menu et exécute l'action choisie par l'utilisateur
print("MENU")
print("1 - Encoder un nom")
print("2 - Décoder un nom")

# Demande à l'utilisateur de choisir une option
choix = input("Faites votre choix (1 ou 2) : ")

# Si l'utilisateur choisit l'encodage
if choix == "1":
    nom = input("Entrez le nom à encoder : ")
    print("Nom encodé :", encoder(nom))

# Si l'utilisateur choisit le décodage
elif choix == "2":
    nom_code = input("Entrez le nom à décoder : ")
    print("Nom décodé :", decoder(nom_code))

# Si l'utilisateur entre autre chose que 1 ou 2
else:
    print("Choix invalide ! Veuillez entrer 1 ou 2.")
