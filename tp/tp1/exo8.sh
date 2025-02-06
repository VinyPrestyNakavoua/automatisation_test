#!/usr/bin/bash
# test : bash tp/tp1/exo8.sh txt

extension_given="$1"
cd tp/tp1/dossierTest
path=$PWD
today=`date +%m-%d-%Y`
files=$(ls "$path")

for file in $files;
do
    if [[ -f $file ]]; then
        filename=$(basename "$file")
        basenom=${filename%.*}
        extension="${filename##*.}"
        if [[ "$extension" == "$extension_given" ]]; then
            extension_added=".$extension_given"
            newfile="$basenom-$today$extension_added"
            echo $file
            echo $newfile
            $(mv $file $newfile)
            echo "Fichier renommé."
            echo ""
        
        fi
    fi

    


done
echo ""
echo "repertoire courant : $path"
echo "extension choisie : $extension_given"
echo "date d'aujourd'hui : $today"


