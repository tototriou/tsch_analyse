import numpy as np
import matplotlib.pyplot as plt
import re

filepath0 = "raw/logs/logs_tsch2.txt"
filepath1 = "raw/logs/logs_tsch10.txt"
filepath2 = "raw/logs/logs_tsch20.txt"
filepath3 = "raw/logs/logs_tsch30.txt"
filepath4 = "raw/logs/logs_tsch40.txt"
filepath5 = "raw/logs/logs_tsch50.txt"

filepath11 = "raw/logs/logs_tsch_32.txt"
filepath12 = "raw/logs/logs_tsch_64.txt"
filepath14 = "raw/logs/logs_tsch_128.txt"
filepath15 = "raw/logs/logs_tsch_256.txt"
filepath13 = "raw/logs/logs_tsch_512.txt"


def parse(filepath, nb_nodes):

    with open(filepath, 'r') as f:
        status = []
        rx = 0
        tx = 0
        for line in f:
            if "[INFO: TSCH-LOG  ]" in line and "uc" in line:
                if "tx LL" in line:
                    tx += 1

                    # info = match.group(1)
                    # extraire le statut
                    # match = re.search(r'st\s+(\d)', info)
                    # if match:
                    #    status.append(int(match.group(1)))
                    #    if int(match.group(1)) == 0:
                    #        nb_success += 1
                if "rx LL" in line:
                    rx += 1
            if "[INFO: TSCH-LOG  ]" in line and "bc" in line:
                if "tx LL" in line:
                    tx += nb_nodes
                if "rx LL" in line:
                    rx += 1
    ratio_success = rx/tx * 100
    return ratio_success

# faire un graphe du taux de fail en fonction de la taille et du nombre de noeuds en utilisant matplotlib


def affiche_nb_nodes():
    # on gradue de 0 a 100 avec un pas de 10 en pourcentage
    # on met un point rouge sur le graphe et une ligne bleu
    # on met un titre au graphe
    # on met un quadrillage
    ratio_success0 = parse(filepath0, 2)
    ratio_success1 = parse(filepath1, 10)
    ratio_success2 = parse(filepath2, 20)
    ratio_success3 = parse(filepath3, 30)
    ratio_success4 = parse(filepath4, 40)
    ratio_success5 = parse(filepath5, 50)

    ratio_success = [ratio_success0, ratio_success1, ratio_success2,
                     ratio_success3, ratio_success4, ratio_success5]
    nb_node = [2, 10, 20, 30, 40, 50]
    plt.plot(nb_node, ratio_success, 'ro', nb_node, ratio_success, 'b')
    plt.title('PDR en fonction du nombre de noeuds')
    plt.grid(True)

    plt.axis([0, 50, 0, 100])
    plt.xlabel('nb_node')
    plt.ylabel('ratio_success')
    plt.show()


def affiche_taille():
    # on gradue de 0 a 100 avec un pas de 10 en pourcentage
    # on met un point rouge sur le graphe et une ligne bleu
    # on met un titre au graphe
    # on met un quadrillage
    ratio_success1 = parse(filepath11, 2)
    ratio_success2 = parse(filepath12, 2)
    ratio_success3 = parse(filepath13, 2)
    ratio_success4 = parse(filepath14, 2)
    ratio_success5 = parse(filepath15, 2)

    ratio_success = [ratio_success1, ratio_success2,
                     ratio_success3, ratio_success4, ratio_success5]
    taille = [32, 64, 128, 256, 512]
    plt.plot(taille, ratio_success, 'ro', taille, ratio_success, 'b')
    plt.title('PDR en fonction de la taille des paquets')
    plt.grid(True)

    plt.axis([0, 550, 0, 100])
    plt.xlabel('taille')
    plt.ylabel('ratio_success')
    plt.show()


def affiche_conso_nb_nodes():
    # on gradue de 0 a 100 avec un pas de 10 en pourcentage
    # on met un point rouge sur le graphe et une ligne bleu
    # on met un titre au graphe
    # on met un quadrillage
    # Ouverture du fichier en mode lecture
    conso = []
    for i in [2, 10, 20, 30, 40, 50]:
        with open(f"raw/consum/conso{i}.txt", "r") as f:
            ligne = f.readline()
            conso.append(float(ligne))

    nb_node = [2, 10, 20, 30, 40, 50]
    plt.plot(nb_node, conso, 'ro', nb_node, conso, 'b')
    plt.title('consommation moyenne en fonction du nombre de noeuds')
    plt.grid(True)

    plt.axis([0, 50, 0, 0.1])
    plt.xlabel('nb_node')
    plt.ylabel('conso')
    plt.show()


def affiche_conso_taille():
    # on gradue de 0 a 100 avec un pas de 10 en pourcentage
    # on met un point rouge sur le graphe et une ligne bleu
    # on met un titre au graphe
    # on met un quadrillage
    # Ouverture du fichier en mode lecture
    conso = []
    for i in [32, 64, 128, 256, 512]:
        with open(f"raw/consum/conso_{i}.txt", "r") as f:
            ligne = f.readline()
            conso.append(float(ligne))

    taille = [32, 64, 128, 256, 512]
    plt.plot(taille, conso, 'ro', taille, conso, 'b')
    plt.title('consommation moyenne en fonction de la taille des paquets')
    plt.grid(True)

    plt.axis([0, 550, 0, 0.1])
    plt.xlabel('taille')
    plt.ylabel('conso')
    plt.show()


def affiche_temps():
    # on gradue de 0 a 100 avec un pas de 10 en pourcentage
    # on met un point rouge sur le graphe et une ligne bleu
    # on met un titre au graphe
    # on met un quadrillage
    # Ouverture du fichier en mode lecture
    temps = [1, 2, 5, 10, 20]
    file = []
    ratio_success = []
    for i in temps:
        file.append(f"raw/logs/logs_tsch_{i}.txt")

    for i in range(len(file)):
        ratio = parse(file[i], 2)
        ratio_success.append(ratio)

    plt.plot(temps, ratio_success, 'ro', temps, ratio_success, 'b')
    plt.title('PDR en fonction du temps inter message')
    plt.grid(True)

    plt.axis([0, 20, 0, 100])
    plt.xlabel('temps')
    plt.ylabel('PDR')
    plt.show()


def affiche_conso_temps():
    # on gradue de 0 a 100 avec un pas de 10 en pourcentage
    # on met un point rouge sur le graphe et une ligne bleu
    # on met un titre au graphe
    # on met un quadrillage
    # Ouverture du fichier en mode lecture
    conso = []
    temps = [1, 2, 5, 10, 20]
    for i in temps:
        with open(f"raw/consum/conso_{i}.txt", "r") as f:
            ligne = f.readline()
            conso.append(float(ligne))

    plt.plot(temps, conso, 'ro', temps, conso, 'b')
    plt.title('consommation moyenne en fonction du temps inter message')
    plt.grid(True)

    plt.axis([0, 20, 0, 0.1])
    plt.xlabel('temps')
    plt.ylabel('conso')
    plt.show()


def affiche_slot():
    # on gradue de 0 a 100 avec un pas de 10 en pourcentage
    # on met un point rouge sur le graphe et une ligne bleu
    # on met un titre au graphe
    # on met un quadrillage
    # Ouverture du fichier en mode lecture
    slot = [100, 200, 397, 500, 600]
    file = []
    ratio_success = []
    for i in slot:
        file.append(f"raw/logs/logs_tsch_s{i}.txt")

    for i in range(len(file)):
        ratio = parse(file[i], 2)
        ratio_success.append(ratio)

    plt.plot(slot, ratio_success, 'ro', slot, ratio_success, 'b')
    plt.title('PDR en fonction de la taille de la slotframe')
    plt.grid(True)

    plt.axis([0, 600, 0, 100])
    plt.xlabel('taille slotframe')
    plt.ylabel('PDR')
    plt.show()


def affiche_conso_slot():
    # on gradue de 0 a 100 avec un pas de 10 en pourcentage
    # on met un point rouge sur le graphe et une ligne bleu
    # on met un titre au graphe
    # on met un quadrillage
    # Ouverture du fichier en mode lecture
    conso = []
    slot = [100, 200, 397, 500, 600]
    for i in slot:
        with open(f"raw/consum/conso_s{i}.txt", "r") as f:
            ligne = f.readline()
            conso.append(float(ligne))

    plt.plot(slot, conso, 'ro', slot, conso, 'b')
    plt.title('consommation moyenne en fonction de la taille de la slotframe')
    plt.grid(True)

    plt.axis([0, 650, 0, 0.1])
    plt.xlabel('taille slotframe')
    plt.ylabel('conso')
    plt.show()


affiche_taille()
affiche_nb_nodes()
affiche_temps()
affiche_slot()
affiche_conso_taille()
affiche_conso_nb_nodes()
affiche_conso_temps()
affiche_conso_slot()
