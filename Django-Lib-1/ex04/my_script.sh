#!/bin/bash

# Créer un VirtualEnv avec Python 3
python3 -m venv django_venv

# Activer le VirtualEnv
source django_venv/bin/activate

# Installer les dépendances à partir du fichier requirement.txt
pip install -r requirement.txt
