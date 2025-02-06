import sys
import os
import json
# exercice 2 : 
# le premier element de sys.argv est le nom du fichier 
if len( sys.argv ) == 1:
    print( "auteur viny presty nakavoua" )
    print( "\tusage: python3 tp1exo2.py string and int values..." )
    exit()

# on doit convertir les strparam en int,  
# car parametres entrés en console sont mis en string par defaut

def appreciation(note):
    if note >= 16:
        return "très-bien"
    elif note >= 14:
        return "bien"
    elif note >= 12:
        return "assez-bien"
    elif note >= 10:
        return "moyen"
    else:
        return "insuffisant"
    

file  = sys.argv[1]
file_directory = os.path.dirname(__file__)
file = file_directory + '\\' + file
with open(file,"r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    linei = lines[i] # it's a list like  ['nom note']
    li_data = linei.split(",")
    data = {"nom": li_data[0], "note" : li_data[1]}
    data["appreciation"] = appreciation(int(li_data[1]))
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)




