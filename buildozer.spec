[app]
# (MANDATAIRE) Le nom de ton application
title = Conciergerie

# (MANDATAIRE) Le nom du package (sans espaces)
package.name = conciergerieapp

# (MANDATAIRE) Le domaine (ex: org.test)
package.domain = org.louis

# (MANDATAIRE) Le dossier source (.)
source.dir = .

# (MANDATAIRE) Les extensions de fichiers à inclure
source.include_exts = py,png,jpg,kv,atlas

# (MANDATAIRE) La version de ton app (l'erreur venait d'ici !)
version = 1.0

# Tes dépendances (Kivy, KivyMD et PyMySQL pour la BDD)
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pymysql

# Orientation de l'écran pour iPhone
orientation = portrait

# --- Paramètres iOS ---
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/ios-control/ios-deploy
ios.ios_deploy_branch = master

[buildozer]
log_level = 2
warn_on_root = 1