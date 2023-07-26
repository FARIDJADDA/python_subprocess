# CRÉER UN TERMINAL AVEC PYTHON

import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat


while True:
    commande = input("Commande : ")
    if commande == "exit":
        break
    
    result = subprocess.run(commande, shell=True, capture_output=True, universal_newlines=True)  # ls sur Linux/macOS
    
    print(result.stdout)
    print(result.stderr)
    