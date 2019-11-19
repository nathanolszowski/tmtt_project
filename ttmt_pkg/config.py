"""
----------------------------------------
------- FICHIER DE CONFIGURATIONS ------
----------------------------------------
# Ce fichier configure le projet TMTT.
"""

import os
# import time


"""
Fonctions gestion des chemins
"""

chemins = dict(
    cheminProjet='/home/nathan/Bureau/TTMT_project/ttmt_project',
    # cheminJava='',
    cheminDicts='/home/nathan/Bureau/TTMT_project/dictionnaire',
    cheminCorpus='/home/nathan/Bureau/TTMT_project/corpus',
    cheminFiches='/home/nathan/Bureau/TTMT_project/fiches',
    cheminLogs='/home/nathan/Bureau/TTMT_project/logs'
)


def test_chemin(cheminRepo):
    """
    Permet de valider ou non accès à un dossier/fichier
    :param cheminRepo : Chemin vers un dossier/fichier
    :return : <str> Validation ou Non
    """
    try:
        os.path.exists(cheminRepo)
        print('Le chemin vers le répertoire ' + cheminRepo + ' a été trouvé')
    except NameError:
        print('!!Le chemin vers le répertoire' + cheminRepo +
              'est introuvable. Vérifiez vos chemins dans votre fichier de configuration!!')


def test_tous_chemins(cheminsRepo):
    """
    Permet de valider accès à tous les dossiers/fichiers
    :param : <dict> Dictionnaire des chemins
    :return : <str> Validation ou non test_chemin()
    """
    for item in cheminsRepo.items():
        test_chemin(str(item))
        print('\n')


"""
Fonctions gestion des temps de traitements
"""

"""
def chrono(ChronoS):
    q, s = divmod(ChronoS, 60)
    h, m = divmod(q, 60)
    j, r = divmod(h, 24)
    if j > 0:
        TempsRestantJHMS = "%d_j %d_h %d_min %d_s" % (j, h, m, s)
    elif h > 0:
        TempsRestantJHMS = "%d_h %d_min %d_s" % (h, m, s)
    elif m > 0:
        TempsRestantJHMS = "%d_min %d_s" % (m, s)
    else:
        TempsRestantJHMS = "%d_s" % (s)
    return TempsRestantJHMS
"""