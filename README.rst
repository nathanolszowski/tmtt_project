============
ttmt_project
============


TTMT is a text mining project to automate classifaction of technicals files.


Description
===========

A longer description of your project goes here...


Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.


Structure TTMT PROJECT
# package/subpackage de fonctions
======================

General - Config :
	Vérifier le chemin d'un fichier/dico
	Vérifier accès à JAVA file
	Accès BDD

--------------------------------------------------------------

Extraire le texte :
	Repérage extension fichier
	Extraction pdf (test avec les différents extracteur)
	Extraction texte
	Extraction nombre pages
	Extraction metadata/infopdf (si existe)
# échec lecture pdf crypté
# échec PDF image
{ input : fichier | output : texte brute

--------------------------------------------------------------

Analyse texte :
	Lemmatisation
	Bigram/Trigram
	Tokennisation
	Stopwords
	Fréquences terme/document
	Normalisation
{ input : texte brute | output : dico de mots

--------------------------------------------------------------

Gestion des dictionnaires :
	Lire un dictionnaire
	Ecrire un dictionnaire
# mots très courants/peu courants/spécialisés
{ input : 

--------------------------------------------------------------

Gestion des logs + FDL :
	Création CSV (FDL)
	Ecrire (FDL)
	Lecture CSV (de logs)
	Ecrire (log)
{ input : logs | output : csv logs
{ input : score/data analyse | output : csv FDL

--------------------------------------------------------------

Score :
	Score % dico
	Classifieur
# Documentation/Loi/Réglementation/Normes
{ input : dico de mots | output : score dico % dicos
{ input : dico de mots | output : catégorie

--------------------------------------------------------------

Gestion base de données/API :
	Lire
	Ecrire
	Conversion JSON
# format JSON
# texte brute/metadata "recherchables"
{ input : fichier traité | output : enregistrement

--------------------------------------------------------------

Interface graphique :
	MainWindow

