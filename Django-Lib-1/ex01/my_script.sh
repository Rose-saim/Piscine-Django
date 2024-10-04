#!/bin/bash

# Afficher la version de pip
pip --version

# Créer un répertoire local_lib si non existant
mkdir -p local_lib

# Installer la bibliothèque path.py à partir de son dépôt GitHub
pip install git+https://github.com/jaraco/path.py.git -t local_lib > install.log 2>&1

# Vérifier l'installation et exécuter le programme Python
if [ $? -eq 0 ]; then
    python3 my_program.py
else
    echo "Installation échouée. Voir install.log pour plus de détails."
fi
