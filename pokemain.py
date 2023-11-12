from bs4 import BeautifulSoup
import requests 
import sys 
import re 
import pypokedex
import random 

SAVE_FOLDER = './output/imgs/'

# get pokemon name
if sys.argv[1] == '-R':
    pokerand = random.randint(1,905)
    pokemonDex = pypokedex.get(dex=pokerand)
else:
    if len(sys.argv) < 2:
        pokemonArg = input("Enter the name of the pokemon to look up: ").title()
    elif len(sys.argv) == 3 :
        pokemonArg = (sys.argv[1] + " " + sys.argv[2]).title()

    else:
        pokemonArg = sys.argv[1].title()

    pokemonDex = pypokedex.get(name=pokemonArg)
    
print(pokemonDex.name)

if pokemonDex.dex < 10 :
    pokeoutput = '00' + str(pokemonDex.dex)
elif pokemonDex.dex >= 10 and pokemonDex.dex < 100:
    pokeoutput = '0' + str(pokemonDex.dex)
else : pokeoutput = str(pokemonDex.dex)


#print('the number is ', pokemonDex) 

# get image

base_image_url = "http://www.serebii.net/swordshield/pokemon/"
full_image_url = base_image_url + pokeoutput + ".png"
response = requests.get(full_image_url)
imagename = SAVE_FOLDER + pokemonDex.name + '.png'
with open(imagename,'wb') as file:
    file.write(response.content)


