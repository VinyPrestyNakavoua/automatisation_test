#!/usr/bin/bash
# test : bash tp/tp1/exo7.sh tp/tp1/

files=$(ls "$1")
nb_rep=0
nb_fichier=0
nb_ex=0

for file in $files
do
    if [ -d "$file" ]; then
        echo "hello viny"
        ((nb_rep++))
    else
        filename=$(basename "$file")
        extension="${filename##*.}"

        if [[ "$extension" == "exe" ]]; then
            ((nb_ex++))
        else
            ((nb_fichier++))
        fi
    fi
done


# Affichage des résultats
echo "Répertoires : $nb_rep"
echo "Fichiers normaux : $nb_fichier"
echo "Fichiers exécutables (.exe) : $nb_ex"
