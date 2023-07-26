# CRÉER UN TERMINAL AVEC PYTHON

import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat


while True:
    commande = input("Commande : ")
    result = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)  # ls sur Linux/macOS
    print(result.stdout)
    if commande == "exit":
        break
    print(result.stderr)
    