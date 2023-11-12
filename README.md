# pokeascii

![Screenshot of Pikachu](./ScreenshotPikachu.png)

A little python and bash script that takes as input a pokemon name and returns its sprite. With the -R flag it returns a random pokemon from any generation. Greatly inspired by [rmccorm4](https://github.com/rmccorm4)'s [Pokefetch](https://github.com/rmccorm4/Pokefetch) project. Thank you for the idea.
Needs [TheZoraiz](https://github.com/TheZoraiz) 's [ascii-image-converter](https://github.com/ascii-image-converter) in order to work.

## Requirements
As listed in the [Requirements.txt](https://github.com/belligerentcrow/pokeascii/Requirements.txt) file: 

* Install [TheZoraiz](https://github.com/TheZoraiz)'s [ascii-image-converter](https://github.com/ascii-image-converter) 

As explained in their repository's [Installation section](https://github.com/TheZoraiz/ascii-image-converter#installation) 

* Beautiful Soup
```
pip install BeautifulSoup
```

* pypokedex
Awesome [project](https://github.com/arnavb/pypokedex) by [arnavb](https://github.com/arnavb)

```
pip install pypokedex
```

* Requests

```
pip install Requests
```

## Installation

1. Clone the repository
```
git clone https://github.com/belligerentcrow/pokeascii.git
```

2. cd into the repository
```sh
cd  ./pokeascii
```

## Use

### By Pokemon name

run the .sh file with the name of a pokemon u want the ascii of with its name as a parameter

```sh
./pokesh.sh <NAME>
```

### Random 

run the .sh file with the -R flag

```sh
./pokesh.sh -R
```

In any case, the script will download the png of the chosen pokemon in the ./output/imgs/ folder, and log the name of the pokemon you've searched in the ./output/log.txt file.

At this point in time, i haven't yet implemented a good error catcher in case of misspells or any of the sort. The output is getting logged. u can just delete it and the images if you dont want extra space on your machine for now. 




