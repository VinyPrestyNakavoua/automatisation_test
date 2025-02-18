#!/usr/bin/bash
# test : bash tp/tp1/exo9.sh tp/tp1/exo9test.py
# on va utiliser les expressions regulières

file=$1
CAT "$file" | grep -v ^#[^!]

