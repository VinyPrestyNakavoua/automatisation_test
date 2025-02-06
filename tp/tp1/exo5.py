import os
import logging
import sys




if len( sys.argv ) == 1:
    print( "auteur viny presty nakavoua" )
    print( "\tusage: python3 triangle.py intValue..." )
    print(
        """
        un script prenant un répertoire et trois entiers en paramètre, et exécutant tous les fichiers python
        contenus dans ce répertoire sur ces trois entiers.
        """

    )


params = sys.argv[1:]
directory = params[0]
entiers = params[1:]




