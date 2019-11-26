
"""
----------------------------------------
------ FICHIER Extraction du texte -----
----------------------------------------
Fonctions extraction du texte
Extraire le texte :
    Extraction pdf (test avec les différents extracteur)
    Extraction texte
    Extraction nombre pages
    Extraction metadata/infopdf (si existe)
# échec lecture pdf crypté
# échec PDF image
# input : fichier | output : texte brute
"""

import os
import io
# conversion pdf to img
from wand.image import Image as Img
try:
    from PIL import Image
except ImportError:
    import Image
# extracteur pdf
import pytesseract
import PyPDF2
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extension_fichier(fichier):
    """
    Permet le repérage de l'extension d'un fichier
    :param : <str> Nom du fichier
    :return : <str> Extension du fichier
    """
    extension = os.path.splitext(fichier)
    extension = extension[1]
    return extension


def convert_pdf(fichier):
    """
    Permet la conversion d'un fichier pdf en fichier image
    :param : <str> Nom du fichier pdf
    :return : <str> Nom du fichier image
    """
    with Img(filename=fichier, resolution=300) as img:
        img.compression_quality = 99
        image = 'image_name.jpg'  # cas ou on traite plusieurs fichiers à la suite
        img.save(filename=image)
    return image


def extraction_pyocr(image):
    """
    Permet l'extraction de pdf image
    :param : <str> Nom du fichier image
    :return : <str> Texte extrait du fichier image
    """
    texte = pytesseract.image_to_string(Image.open(image), lang='eng')
    print(texte)
    return texte


def extraction_PyPDF2(fichier):
    """
    Permet l'extraction de fichier pdf de niveau facile
    :param : <str> Nom du fichier pdf
    :return : <str> Texte extrait du fichier pdf
    """
    print('---- > Ouverture du fichier PdF avec le moteur PyPDF2')
    # erreurPdF=0
    # try:
    readerPyPDF2 = PyPDF2.PdfFileReader(fichier, strict=False)
    # except ValueError :
#        print('Erreur moteur PyPDF2'+str(ValueError))
#        erreurPdF=1
    #    pass
    if readerPyPDF2.isEncrypted == True:
        print('!! Document crypté')
        log_writer.writerow(('>> ' + 'Echec lecture texte crypté : ' + TitreTexte +
                             ' type : ' + extension, (time.time() - start_time)))
    # if erreurPdF==0:
    num_page = readerPyPDF2.numPages
    infoPdf = readerPyPDF2.getDocumentInfo()

    print('---- > Extraction Entête PdF')
    for nd in readerPyPDF2.namedDestinations:
        print(nd)
    return (readerPyPDF2, num_page, infoPdf)


def extraction_PDFMiner(fichier):
    """
    Permet l'extraction de fichier pdf de niveau intermédiaire
    :param : <str> Nom du fichier pdf
    :return : <str> Texte extrait du fichier pdf
    """
    print('---- > Ouverture du fichier PdF avec le moteur PDFMiner')
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(fichier, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            num_page += 1
            page_interpreter.process_page(page)
        texte = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()
    return (texte, num_page)
