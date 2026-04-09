import sys
import os

# On ajoute le dossier login au chemin de recherche
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'login')))

# On lance l'application depuis login.py
from login import ConciergerieApp

if __name__ == "__main__":
    ConciergerieApp().run()