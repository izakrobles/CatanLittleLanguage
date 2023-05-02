# CatanLittleLanguage
### CSCI 3200 Final Project

## What is this?
This is a project built on the Python Lark tool. It defines a grammar for the popular board game *Catan*. The game begins with "start game {list of players}". Each player must begin their turn with rolling dice. Once a player has rolled dice, their turn can end, or they can take an action. Actions include drawing a development card (knight, victory, year of plenty, monopoly, road building), building a structure (road, city, or settlement), trading resources (brick, lumber, wool, grain, or ore), or using a development card. (Note: players can take more than one action per turn).

## What is in this directory
- `README.md`: This file, which provides an overview of the project.
- `formatting.md`: A file containing formatting specifications for phrases allowed in the language.
- `lark.txt`: A file containing the grammar specification for the Catan Little Language.
- `parser.py`: The main Python script that processes input files and outputs the game results.
- `game_one.txt`, `game_two.txt`, `game_three.txt`: Sample input files containing sequences of gameplay actions.

## How do you use it?
1. Ensure that you have Python 3 installed on your machine.
2. Run the parser script with an input file as an argument, e.g. `python3 parser.py game_one.txt`.
3. The script will output the results of the game, including a leaderboard and a declaration of leader/winner.

