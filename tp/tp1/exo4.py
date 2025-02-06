import os
import sys
import logging


if len( sys.argv ) == 1:
    print( "auteur viny presty nakavoua" )
    print( "\tusage: python3 triangle.py intValue..." )
    print(
        """
        un script qui crée 5 fichiers fic1.txt à fic5.txt, contenant respectivement les valeurs 1 à 5, dans un
        répertoire passé en paramètre.
        Si ce répertoire n’existe pas, il doit être créé. Si un des cinq fichiers existe déjà, un message d’erreur doit être
        affiché.
        """
    )
    logging.critical("vous devez entrer un dossier ou un chemin de dossiers")

    exit()


def create_files():
    """
    fonction qui crée et ecris dans les 5 fichiers
    """

    files = ["fic1.txt", "fic2.txt", "fic3.txt", "fic4.txt", "fic5.txt"]
    for i in range(len(files)):
        with open(files[i], "w") as f:
            f.write(str(i+1))

directory = sys.argv[1]
directory = str(directory)
os.chdir("./tp/tp1/")   # pour que les dossiers et fichiers sont creer dans tp1
# verifions si le dossier
if not os.path.exists(directory):
    os.makedirs(directory)

# allez dans le dossier de travail où on va creer les fichiers
os.chdir("./"+directory)
create_files()












