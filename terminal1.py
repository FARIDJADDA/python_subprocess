# CRÉER UN TERMINAL AVEC PYTHON

import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat
result = subprocess.run("dir", shell=True, capture_output=True)  # ls sur Linux/macOS

print(result.stdout.decode("utf-8", errors="ignore"))