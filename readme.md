
# Automate-contact

C'est un script python qui automatise l'enregistrement des contacts sur un compte Gmail. pour ce faire suivez les étapes ci-après :

# 1. Activer l'API Google
* Accéder à la console google sur ce lien [Google Cloud Console](console.cloud.google.com)
* Créer un nouveau projet ou utiliser un projet déjà existant
* Recherchez et activez l'API People (pour Google Contacts).
* Configurer les autorisation OAuth 2.0 pour pouvoir obtenir un fichier json ( qu'on appelera credentials.json)
* Placer le fichier `credentials.json`à la racine du projet

# 2. Configurer l'écran de consentement OAuth
## - Choisissez votre Type d'utilisateur :

*Sélectionnez "Interne" si vous utilisez un compte professionnel ou scolaire Google Workspace.
Sélectionnez "Externe" si vous utilisez un compte Gmail normal.

## - Informations de base :

* Nom de l'application : "Gestionnaire de contacts (script Python)" ou un nom similaire.

* Adresse e-mail de support utilisateur : Utilisez votre adresse e-mail.

* Logo de l'application : (Facultatif, vous pouvez laisser vide pour un script personnel.)

* Domaine : Laissez vide si vous n’avez pas de site web associé.
* Liens :
* Politique de confidentialité : Ajoutez un lien (ou un faux, comme https://example.com pour un usage personnel).

* Conditions d'utilisation : Laissez vide ou ajoutez un lien fictif si requis.

* Domaine de l’application : Laissez vide (non nécessaire pour un script personnel).

## Périmètres OAuth (Scopes) :

Ajoutez https://www.googleapis.com/auth/contacts pour gérer vos contacts.
(Vous pouvez ignorer les autres scopes pour ce script.)

## Informations de test :

* Utilisateurs testeurs :Ajoutez des adresses mails auxquelles vous avez accès. ou la votre (Cela évite que Google marque votre application comme "non vérifié".
* Vous pouvez ajouter jusqu'à 100 utilisateurs testeurs en mode test.

# 3. Créer des Identifiants OAuth
### Type d'application :

Choisissez "**Application de bureau**" ou "Autre" (idéal pour un script local).

Nom de l'application : Donnez un nom descriptif pour ne pas oublier, comme "Script gestionnaire de contacts".

Identifiants générés :

Téléchargez le fichier `credentials.json`. Ce fichier contient votre client ID et votre secret.

# 4. Installer toutes les dépendances python
À la racine du projet, Éxecuter cette commande : `pip install -r requirements.txt`


# 5. Préparation des contacts
Assurer vous d'avoir vos contacts stockés soit dans un fichier excel, un fichier csv, ou une structure python (Liste des dictionnaires)

    le fichier doit comporter au minimum 2 colonnes : "Nom" et " Téléphone" sous cette forme 

# 6. Instruction de lancement
* Placer le fichier `credentials.json`à la racine du projet
* lancer le Script de votre choix, vous serez appeler à vous conectez via google
* une fois la configuration effectué un fichier `token.json`sera créé pour vous éviter de vous reconnecter à chaque fois

