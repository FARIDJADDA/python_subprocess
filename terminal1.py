# CRÉER UN TERMINAL AVEC PYTHON

import subprocess

# Popen : ancienne interface
# run : executer la commande et attendre le résultat
result = subprocess.run("dir", shell=True, capture_output=True, universal_newlines=True)  # ls sur Linux/macOS

print(result.stdout)
print(result.stderr)