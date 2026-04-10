[app]
# (IMPORTANT) Le dossier source est le dossier actuel (.)
source.dir = .

# (IMPORTANT) Assure-toi que TOUS tes dossiers sont inclus
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = images/*,utilisateur/*,login/*,recherche/*

# (IMPORTANT) Vérifie la ligne requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pymysql

# Le nom de ton package (ne doit pas contenir d'espaces)
package.name = conciergerieapp
package.domain = org.hackathon