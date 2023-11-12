#!/bin/bash

# make output dir
mkdir -p output

echo $@

# get pokemon stat and output to file
/usr/bin/env python3 pokemain.py $@ >> output/log.txt

# format input
#POKEMON=${./output/log.txt}  # $@ = command line argument
POKEMON=$( tail -n 1 ./output/log.txt )

#POKELOWERCASE=$POKEMON | tr '[:upper:]' '[:lower:]'
POKELOWCASE="${POKEMON,,}"

# get image and output to fil"e
# catimg -w 120 "imgs/$POKEMO.png" > output/image.txt

exec ascii-image-converter -C output/imgs/$POKELOWCASE.png 