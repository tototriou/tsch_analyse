import subprocess
import json

# Exécute la commande iotlab-status
command_output = subprocess.check_output(
    ["iotlab-status", "--nodes", "--site", "strasbourg", "--archi", "m3"])

# Parse le résultat JSON
data = json.loads(command_output)


nodes = []

clients = data["items"]
for c in clients:
    if c["state"] == "Alive":
        nodes.append(c["network_address"][3:-24])


#Ouverture du fichier en mode écriture
with open("nodes.txt", "w") as f:
    # Écrit chaque élément de la liste sur une nouvelle ligne
    for item in nodes:
        f.write(item + "\n")
