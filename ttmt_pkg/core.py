"""
-----------------------------------------------------------------------------
=============================================================================
----------- TMTT - Text Mining de Textes Techniques - 09/2019- --------------
---------------------------------JRubio--------------------------------------
=============================================================================

----------------------------------------
------------ FICHIER CORE --------------
----------------------------------------
"""

import config as cfg
import analyse_text as at
import extract_text as et
# from progress.bar import IncrementalBar

print('Hello World \n')
print('----> Vérification des accès aux différents dossiers \n')

cfg.test_tous_chemins(cfg.chemins)  # Test de la configuration

print('----> Début de l\'analyse textuelle \n')

# bar = IncrementalBar('Processing', max=20)
# for i in range(20):
#    bar.next()
texte = et.extraction_pyocr('EchecPdF.jpg')
print('\n')
instance = at.Traitement(texte)

# bar.finish()
