# CatanLittleLanguage
### CSCI 3200 Final Project

## What is this?
This is a project built on the Python Lark tool. It defines a grammar for the popular board game *Catan*. If you run the `CatanLeaderboard.py` file on a '.txt' file it will parse the language within the `.txt` file. If it is a valid input, it will return a leaderboard and a winner based on the what happens in the gameplay within the `.txt` file. 

## What is in this directory
- `CatanLeaderboard.py`: The main Python script that processes input files and outputs the game results.
- `formatting.md`: A file containing formatting specifications for phrases allowed in the language.
- `lark.txt`: A file containing the raw grammar specification for the Catan Little Language.
- `game_one.txt`, `game_two.txt`, `game_three.txt`: Sample input files containing sequences of gameplay actions.
- `README.md`: This file, which provides an overview of the project.

## How do you use it?
1. Ensure that you have Python 3 installed on your machine.
2. Run the CatanLeaderboard script with an input file as an argument, e.g. `python3 CatanLeaderboard.py game_one.txt`.
3. The script will output the results of the game, including a leaderboard and a declaration of leader/winner.
4. Feel free to create your own game script and save it to a new `.txt` file and just tag it when calling the `CatanLeaderboard.py`

