
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


def extension_fichier(nom):
    """
    Permet le repérage de l'extension d'un fichier
    :param : <str> Nom du fichier
    :return : <str> Extension du fichier
    """
    extension = os.path.splitext(nom)
    extension = extension[1]
    return extension


"""
def ExtractionPDF_PyPDF2(pdfFileObjPyPDF2,TitreTextePyPDF2):
    print('---- > Ouverture du fichier PdF avec le moteur PyPDF2')
    #erreurPdF=0
    #try:
    pdfReaderPyPDF2 = PyPDF2.PdfFileReader(pdfFileObjPyPDF2, strict=False)
    #except ValueError :
#        print('Erreur moteur PyPDF2'+str(ValueError))
#        erreurPdF=1       
    #    pass
    if pdfReaderPyPDF2.isEncrypted==True:
        print('!! Document crypté')
        Log_writer.writerow(('>> '+'Echec lecture texte crypté : '+TitreTexte+' type : '+extentionFichier,(time.time() - start_time)))
    #if erreurPdF==0:
    num_pagesPyPDF2 = pdfReaderPyPDF2.numPages
    InfoPDFPyPDF2 = pdfReaderPyPDF2.getDocumentInfo()
    print('---- > Extraction Entête PdF')
    for nd in pdfReaderPyPDF2.namedDestinations:
        print(nd)
    return (pdfReaderPyPDF2,num_pagesPyPDF2,InfoPDFPyPDF2)


def ExtractionPDF_PDFMiner(pdfFileObjPDFMiner,TitreTextePDFMiner):
    print('---- > Ouverture du fichier PdF avec le moteur PDFMiner')
    num_pagesPDFMiner=0
    #def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(pdfFileObjPDFMiner, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True,check_extractable=True):
            num_pagesPDFMiner +=1
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()
    if text:
        return (text,num_pagesPDFMiner)
"""
