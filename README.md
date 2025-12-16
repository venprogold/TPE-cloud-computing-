# TPE-cloud-computing-
LISTE DES MEMBRES ET PARTICIPATION :

1)  FANDO BIENVENUE FIYAMA 23B423FS :mise en place sur GitHub et explications de la résolution 
2)  WANDALA ISAAC 23A765FS: conception de l'algorithme 6 et 11
3)  NDEWELEM MATTHIEU 23B195FS : conception de l'algorithme 11 et 23
4)  TCHIDEME GABRIEL 23B036FS : mise en place sur GitHub et explication de la résolution
5)  GUIDAIDI ALAHOKI 23BO69FS: résolution de l'algorithme 6,11 et 23
6)  GANDI HASSAN KAVAYE ALPHONSE  23B053FS : résolution de l'algorithme 6 et 11

<h1>Présentation générale </h1>

Ce projet regroupe trois algorithmes fondamentaux développés en Python. Chaque algorithme répond à un problème précis :

#### la validation d’une adresse IP,
#### le chiffrement César,
#### le jeu du Pendu.


Ce fichier README explique clairement le rôle de chaque algorithme, son fonctionnement, et la manière de l’utiliser.


----------------------------------
## 1. Algorithme de validation d’adresse IP

<h2> Problème posé: </h2>

Vérifier si une chaîne de caractères saisie par l’utilisateur correspond à une adresse IPv4 valide.

<h2> Principe de résolution </h2>

Une adresse IPv4 valide doit respecter les règles suivantes :

-> être composée de 4 parties séparées par des points .

-> chaque partie doit être un nombre entier

-> chaque nombre doit être compris entre 0 et 255


<h2> L’algorithme :</h2>

1. découpe l’adresse IP en parties à l’aide du séparateur .
2. vérifie qu’il y a exactement 4 parties
3. contrôle que chaque partie est numérique
4. vérifie que chaque valeur est dans l’intervalle autorisé

<h2> Utilisation </h2>

adresse_ip_valide("192.168.1.1")  # True
adresse_ip_valide("300.10.2.1")   # False

<h2>Résultat attendu</h2>

True si l’adresse IP est valide
False sinon

----------------------------------
## 2. Algorithme de chiffrement César

<h2> Problème posé</h2>

Sécuriser un texte en le rendant illisible à l’aide d’un décalage des lettres dans l’alphabet.

<h2> Principe de résolution</h2>

Le chiffrement César consiste à :
->décaler chaque lettre de 3 positions dans l’alphabet
->conserver la casse (majuscule/minuscule)
->ne pas modifier les caractères non alphabétiques

<h2> L’algorithme :</h2>

1. parcourt chaque caractère du texte
2. vérifie s’il s’agit d’une lettre
3. applique un décalage circulaire de 3 lettres
4. reconstruit le texte chiffré

<h2> Utilisation </h2>

encoder("Bonjour")  # "Erqmrxu"

<h2> Résultat attendu </h2>

Un texte chiffré, plus difficile à lire sans connaître la clé de décalage.

----------------------------------
## 3. Algorithme du jeu du Pendu

<h2>Problème posé</h2> 

Créer un jeu interactif où l’utilisateur doit deviner un mot caché lettre par lettre avec un nombre limité d’essais.

<h2> Principe de résolution</h2>

Le jeu du pendu repose sur :
un mot secret
un ensemble de lettres déjà proposées
un nombre maximal d’erreurs autorisées

<h2> L’algorithme :</h2>

1. choisit un mot à deviner
2. affiche les lettres trouvées et des _ pour les autres
3. demande une lettre à l’utilisateur
4. vérifie si la lettre est dans le mot
5. décrémente les essais en cas d’erreur
6. s’arrête quand le mot est trouvé ou que les essais sont épuisés

<h2> Utilisation</h2>

Lancer le programme et suivre les instructions à l’écran :

entrer une lettre

observer l’évolution du mot

Résultat attendu

Victoire : le mot est entièrement découvert

Défaite : le nombre d’essais est épuisé

