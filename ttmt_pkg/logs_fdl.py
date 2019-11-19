"""
----------------------------------------
------- FICHIER DE LOGS ET FICHES ------
----------------------------------------
Ecriture des logs et fiche de lecture

Gestion des logs + FDL :
    Création CSV (FDL)
    Ecrire (FDL)
    Lecture CSV (de logs)
    Ecrire (log)
# input : logs | output : csv logs
# input : score/data analyse | output : csv FDL
"""

import config as cfg
import csv


def lecture_csv_liste(nom, chemin=str(cfg.chemins['cheminDicts'])):
    """
    Permet la lecture d'un fichier CSV
    :param : <str> Nom du fichier à lire
    :param : <str> Chemin vers le dossier / par défaut celui des dicts
    :return : <list> Liste de mots pour analyse
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
    :param : <str> Nom du fichier à créer
    :param : <str> Chemin vers le dossier / par défaut celui des logs
    :return : Fichier CSV
    """
    nom = chemin + '/' + nom + '.csv'
    file = open(nom, "wb")
    file.close()
    return 'Le fichier ' + nom + ' a été créé'


def ecriture_log():
    """
    Permet la complétion du fichier de logs
    :param : <str> Nom du fichier de logs
    :param : <str> Chemin vers le dossier / par défaut celui des logs
    :param : Liste des metadata à entrer dans le fichier
    """
    pass


def ecriture_fiche():
    """
    Permet la création et l'écriture d'une fiche de lecture
    :param : <str> Nom du fichier de logs
    :param : <str> Chemin vers le dossier / par défaut celui des logs
    :param : Liste des metadata à entrer dans le fichier
    """
    pass
