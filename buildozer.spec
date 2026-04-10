[app]
# (OBLIGATOIRE) Les infos de base
title = Conciergerie
package.name = conciergerieapp
package.domain = org.louis
version = 1.0
icon.filename = icone_app.png

# (OBLIGATOIRE) Sources et dépendances
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pymysql

# --- PARAMÈTRES iOS (C'est ici que l'erreur se trouvait) ---
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/ios-control/ios-deploy
ios.ios_deploy_branch = master

# AJOUTE CETTE LIGNE POUR CORRIGER LE CRASH
ios.codesign.allowed = 0

# Paramètres d'affichage
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1