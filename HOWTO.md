Sail Race: Outils
=================

## Pré-requis

- Python 3 (testé avec 3.7.7)
- `pip`
- recommendé: activer `virtualenv`
- packages listés dans [`requirements.txt`](./requirements.txt), à installer avec :

  ```shell
  > pip install -r requirements.txt
  ```

## Installation

Installer l'outil `sail-race` avec :

```shell
> pip install -e .
```

## Syntaxe globale

```shell
> sail-race --help
usage: sail-race [-h] {play,tables,boat,compass,map} ...

Sail Race.

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  {play,tables,boat,compass,map}
    play                Prepare game
    tables              Generate tables
    boat                Generate boat token (format is PNG)
    compass             Generate compas rose (format is PNG)
    map                 Generate map of hexes (format is PNG)

Use -h/--help after subcommand for help on subcommand arguments.
```

### Grille de jeu

```shell
> sail-race map --help
usage: sail-race map [-h] [-o OUTPUT] [-r RADIUS] [-S HEX_SIZE] [-s SEED]

Generate map of hexes (format is PNG)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        ignore for STDOUT (default: <_io.BufferedWriter name='<stdout>'>)
  -r RADIUS, --radius RADIUS
                        radius of map in number of hexes (default: 12)
  -S HEX_SIZE, --hex-size HEX_SIZE
                        radius of one hex in pixels (default: 24)
  -s SEED, --seed SEED  ignore for random seed (systime based) (default: None)
````

Par exemple:

- ```bash
  sail-race map -s 0
  ```

  génère le contenu du fichier [MAP\[0\].png](./components/MAP[0].png).

### Plateau de la rose des vents

```shell
> sail-race compass --help
usage: sail-race compass [-h] [-o OUTPUT]

Generate compass rose (format is PNG)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        ignore for STDOUT (default: <_io.BufferedWriter name='<stdout>'>)
```

Génère l'image contenue dans le fichier [COMPASS.png](./components/COMPASS.png).

### Jeton bateau

```shell
> sail-race boat --help
usage: sail-race boat [-h] [-o OUTPUT]

Generate boat token (format is PNG)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        ignore for STDOUT (default: <_io.BufferedWriter name='<stdout>'>)
```

Génère l'image contenue dans le fichier [BOAT.png](./components/BOAT.png).

### Tables de génération aléatoire

```shell
> sail-race tables --help
usage: sail-race tables [-h]

Generate tables

optional arguments:
  -h, --help  show this help message and exit
```

Génère le contenu du fichier [TABLES](./components/TABLES).

### Tables météo pré-tirées

```shell
> sail-race play --help
usage: sail-race play [-h] [-s SEED] -n COUNT [-i INITIAL_BEARING]

Prepare game

optional arguments:
  -h, --help            show this help message and exit
  -s SEED, --seed SEED  ignore for random seed (systime based) (default: None)
  -n COUNT, --count COUNT
  -i INITIAL_BEARING, --initial-bearing INITIAL_BEARING
                        ignore for random initial bearing (default: None)
```

Par exemple:

- ```bash
  sail-race play -s 0 -n 100
  ```

  génère le contenu du fichier [PLAY\[0\]:100](./components/PLAY[0]:100) (cap initial aléatoire).

- ```bash
  sail-race play -s 1 -n 50 -i 55
  ```

  génère le contenu du fichier [PLAY:55\[1\]:50](./components/PLAY:55[1]:50) (cap initial prédéfini).
