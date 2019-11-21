"""
----------------------------------------
------------ FICHIER SCORING------------
----------------------------------------

Score :
	Score % dico
	Classifieur
# Documentation/Loi/Réglementation/Normes
# input : dico de mots | output : score dico % dicos
# input : dico de mots | output : catégorie
"""

# sklearn for preprocessing and machine learning models
from sklearn.feature_extraction.text import TfidfVectorizer


def tfxidf(texte):
	vectorizer = TfidVectorizer()
    X_train = vectorizer.fit_transform(texte)
    X_val = vectorizer.transform(X_val)
    X_test = vectorizer.transform(test_set['cleaned_text'])
