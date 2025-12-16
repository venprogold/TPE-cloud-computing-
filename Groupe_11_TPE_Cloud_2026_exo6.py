
# FONCTION : adresse_ip_valide
# Rôle : vérifier si une adresse IP est valide (IPv4)
# Format attendu : X.X.X.X
# Chaque X doit être un nombre compris entre 0 et 255
def adresse_ip_valide(ip):

    # Sépare la chaîne de caractères en utilisant le point "."
    # Exemple : "192.168.1.1" → ["192", "168", "1", "1"]
    parties = ip.split(".")

    # Vérifie que l'adresse contient exactement 4 parties
    if len(parties) != 4:
        return False

    # Parcourt chaque partie de l'adresse IP
    for partie in parties:

        # Vérifie que la partie contient uniquement des chiffres
        # (pas de lettres, ni de symboles)
        if not partie.isdigit():
            return False

        # Convertit la partie en nombre entier
        nombre = int(partie)

        # Vérifie que le nombre est compris entre 0 et 255 inclus
        if nombre < 0 or nombre > 255:
            return False

    # Si toutes les vérifications sont correctes, l'adresse est valide
    return True


# PROGRAMME PRINCIPAL
# Demande une adresse IP à l'utilisateur et affiche le résultat
# Saisie de l'adresse IP par l'utilisateur
ip = input("Entrez une adresse IP : ")

# Appel de la fonction de vérification
if adresse_ip_valide(ip):
    print(" Adresse IP VALIDE")
else:
    print(" Adresse IP INVALIDE")
