"""
----------------------------------------
-------- FICHIER ANALYSE TEXTE ---------
----------------------------------------
Analyse texte :
    Tokenisation
    # Bigram/Trigram > graph of words
    Fréquences terme/document > TF
    Normalisation > IDF
    Similarité cosinus
"""

# Standard packages
import os
import pickle
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import string
import re
# import TextBlob

# nltk
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer


class Traitement:
    def __init__(self, n):
        self.x = n
        self.supp_maj()
        self.supp_nb()
        self.supp_ponc()
        self.supp_espace()
        self.token()
        print(self.x)

    def supp_maj(self):
        """
        Permet le passage de tout le texte en minuscule
        :param : <str> Le texte à parser
        :return : <str> Le texte sans la casse
        """
        self.x = self.x.lower()

    def supp_nb(self):
        """
        Permet la suppression de tous les nombres du texte
        :param : <str> Le texte à parser
        :return : <str> Le texte sans les nombres
        """
        self.x = re.sub(r'\d+', '', self.x)

    def supp_ponc(self):
        """
        Permet la suppression de toute la ponctuation du texte
        :param : <str> Le texte à parser
        :return : <str> Le texte sans la ponctuation
        """
        table = str.maketrans({key: None for key in string.punctuation})
        self.x = self.x.translate(table)

    def supp_espace(self):
        """
        Permet la suppression de tous les espaces du texte
        :param : <str> Le texte à parser
        :return : <str> Le texte sans les espaces inutiles/invisibles
        """
        self.x = self.x.strip()

    def token(self):
        """
        Permet la tokenization de tout le texte
        :param : <str> Le texte à parser
        :return : <list> Le texte tokenisé
        """
        self.x = word_tokenize(self.x)


def stopword(texte):
    """ 
    Permet la suppression des stopwords (mots vides)
    :param : <list> Le texte tokenizé
    :return : <list> Le texte tokenizé sans 
    """
    stop_words = set(stopwords.words('french'))
    tokens = word_tokenize(texte)
    result = [i for i in tokens if not i in stop_words]
    return result


def stemming(texte):
    stemmer = PorterStemmer()
    texte = word_tokenize(texte)
    for word in texte:
        print(stemmer.stem(word))
    return texte


def lemmatization(texte):
    lemmatizer = WordNetLemmatizer()
    input_str = word_tokenize(input_str)
    for word in input_str:
        print(lemmatizer.lemmatize(word))
    return texte


def partofspeech(texte):
    texte = TextBlob(texte)
    print(texte.tags)
    return texte
