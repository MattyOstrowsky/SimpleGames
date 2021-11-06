
# Simple python games
<img align="right" width="33%" src="https://cdn-icons-png.flaticon.com/512/2780/2780137.png">

## Table of contents

* [General info](#general-info)
* [Installation](#installation)
* [How to run it](#how-to-run-it)
* [License](#license)

## General info
### wisielec (hangman)
The hanged man game. I don't think it's necessary to explain :)
### labirynt (maze game)
A simple game of finding the treasure and u have five lives.
### balista (ballistic)
You play as a tanker. Your task is to choose the right angle and bullet speed. By choosing the distance of the target the task is to hit. Graphical representation on the chart.

## Installation

1. Git clone repository:
```bash
$ git clone https://github.com/gunater/SimpleGames.git
```
2. Install the necessary python dependencies you can use `pipenv`:
```bash
$ pipenv install
$ piipenv shell
```
or you can install from requirements.txt with `pip`:
```bash
$ pip install -r requirements.txt
```
## How to run it
To run the script, go to the main directory:
```bash
$ cd <gamepath>/
```
In place of `<gamepath>`, type `balista`, `labirynt` or `wisielec`
and then run script if its hangman:
```bash
$ python3 main.py
```
else, if its maze game:
```bash
$ python3 game.py
```
or if its ballistic:
```bash
$ python3 balista.py
```

#Good luck and have fun !!
## License
All code is licensed under an MIT license. This allows you to re-use the code freely, remixed in both commercial and non-commercial projects. The only requirement is to include the same license when distributing.

