"""

Ecriture des logs et fiche de lecture

"""

import config as cfg
import csv


def lecture_CSV(nom, chemin=str(cfg.chemins['cheminLogs'])):
    """
    Permet la lecture d'un fichier CSV
    """
    fichierCSV = '/' + chemin + nom
    cfg.test_chemin(fichierCSV)
    print('Ouverture du fichier ' + nom)

    file = open(nom, 'r')
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        listeMots = set(row)
    file.close()
    return listeMots


def nouveau_csv(nom, chemin=str(cfg.chemins['cheminLogs'])):
    """
    Permet la création d'un fichier CSV
    """
    nom = chemin + '/' + nom + '.csv'
    file = open(nom, "wb")
    file.close()
    return 'Le fichier ' + nom + ' a été créé'
