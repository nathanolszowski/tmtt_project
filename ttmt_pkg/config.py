# ----------------------------------------
# -- FICHIER DE CONFIGURATIONS --
# ----------------------------------------

# Ce fichier configure les repertoires utilisés dans le programme

import os


chemins = dict(
    cheminProjet='/home/nathan/Bureau/TTMT_projectttmt_project',
    # cheminJava='',
    cheminDicts='',
    cheminCorpus='',
    cheminFiches=''
)


def TestChemin(chemin):
        # valider ou non accès aux fichiers
    try:
        os.path.exists(chemin)
        print('Le chemin vers le répertoire' + chemin + 'a été trouvé')
    except NameError:
        print('!!Le chemin vers le répertoire' + chemin +
              'est introuvable. Vérifiez vos chemins dans votre fichier de configuration!!')


def TestAcces(cheminsRepo):
        # valider accès à tous les dossiers
    for item in cheminsRepo:
        TestChemin(item)
        print('\n')
