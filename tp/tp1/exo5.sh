#!/usr/bin/bash
# bash tp/tp1/exo5.sh ./tp/tp1/fichiers 5 4 6
directory="$1"

files=$(ls "$directory")
for file in $files
do
    "C:/Program Files/python/python.exe" "$directory"/$file $2 $3 $4
done

exit 0
