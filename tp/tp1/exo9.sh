#!/usr/bin/bash
# test : bash tp/tp1/exo9.sh tp/tp1/exo9test.py
# on va utiliser les expressions regulières

file=$1
cleaned_file="cleaned_$(basename "$file")"

# Garde le shebang intact, retire les commentaires
awk '
  # Si la ligne commence par "#", c'est un commentaire, on le supprime
  # Sauf si la ligne commence par "#!" (le shebang)
  !/^#!/ && /^#/ { next }
  # Retirer les commentaires en ligne (tout après un "#" sauf pour le shebang)
  { sub(/#.*/, "") }
  # Afficher la ligne modifiée
  { print }
' "$file" > "$cleaned_file"
