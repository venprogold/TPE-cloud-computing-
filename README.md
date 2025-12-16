# TPE-cloud-computing-
LISTE DES MEMBRES ET PARTICIPATION :

1) FANDO BIENVENUE FIYAMA 23B423FS
(
2) WANDALA ISAAC 23A765FS
3)  NDEWELEM MATTHIEU 23B195FS

## Présentation générale

Ce projet regroupe trois algorithmes fondamentaux développés en Python. Chaque algorithme répond à un problème précis :

#### la validation d’une adresse IP,
#### le chiffrement César,
#### le jeu du Pendu.


Ce fichier README explique clairement le rôle de chaque algorithme, son fonctionnement, et la manière de l’utiliser.



## 1. Algorithme de validation d’adresse IP

### Problème posé:

Vérifier si une chaîne de caractères saisie par l’utilisateur correspond à une adresse IPv4 valide.

### Principe de résolution

Une adresse IPv4 valide doit respecter les règles suivantes :

-> être composée de 4 parties séparées par des points .

-> chaque partie doit être un nombre entier

-> chaque nombre doit être compris entre 0 et 255


### L’algorithme :

1. découpe l’adresse IP en parties à l’aide du séparateur .
2. vérifie qu’il y a exactement 4 parties
3. contrôle que chaque partie est numérique
4. vérifie que chaque valeur est dans l’intervalle autorisé

### Utilisation

adresse_ip_valide("192.168.1.1")  # True
adresse_ip_valide("300.10.2.1")   # False

### Résultat attendu

True si l’adresse IP est valide
False sinon


## 2. Algorithme de chiffrement César

### Problème posé

Sécuriser un texte en le rendant illisible à l’aide d’un décalage des lettres dans l’alphabet.

### Principe de résolution

Le chiffrement César consiste à :
->décaler chaque lettre de 3 positions dans l’alphabet
->conserver la casse (majuscule/minuscule)
->ne pas modifier les caractères non alphabétiques

### L’algorithme :

1. parcourt chaque caractère du texte
2. vérifie s’il s’agit d’une lettre
3. applique un décalage circulaire de 3 lettres
4. reconstruit le texte chiffré

### Utilisation

encoder("Bonjour")  # "Erqmrxu"

### Résultat attendu

Un texte chiffré, plus difficile à lire sans connaître la clé de décalage.


## 3. Algorithme du jeu du Pendu

### Problème posé

Créer un jeu interactif où l’utilisateur doit deviner un mot caché lettre par lettre avec un nombre limité d’essais.

### Principe de résolution

Le jeu du pendu repose sur :
un mot secret
un ensemble de lettres déjà proposées
un nombre maximal d’erreurs autorisées

### L’algorithme :

1. choisit un mot à deviner
2. affiche les lettres trouvées et des _ pour les autres
3. demande une lettre à l’utilisateur
4. vérifie si la lettre est dans le mot
5. décrémente les essais en cas d’erreur
6. s’arrête quand le mot est trouvé ou que les essais sont épuisés

### Utilisation

Lancer le programme et suivre les instructions à l’écran :

entrer une lettre

observer l’évolution du mot

### Résultat attendu

Victoire : le mot est entièrement découvert

Défaite : le nombre d’essais est épuisé

