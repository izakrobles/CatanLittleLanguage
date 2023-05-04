from lark import Lark
import sys
import os

if len(sys.argv) < 2:
    print("Error: Please provide a file path as a command line argument.")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' does not exist.")
    sys.exit(1)

with open(file_path, 'r') as file:
    game = file.read()


catan_grammar = """
start: "start game" players turn* | turn+

players: player | players (","|"and"|",""and")? player
player: /[A-Za-z]+/

turn: player die_roll ("and" action)*

die_roll: "rolls" dice_digits

action: draw
    | build
    | trade
    | use_card
    | achieve

draw: "draws" dev_card "development card"

build: "builds" structure "at" location

trade: "trades" resources "with" player "for" resources

use_card: "uses" dev_card "card"

achieve: "gets" special "achievement"

structure: "road" -> road | "settlement" -> settlement | "city" -> city
location: "{" NUMBER "," NUMBER "}"

resource_item: NUMBER resource
resources: resource_item | resource_item (","|"and"|",""and")? resources

resource: "brick"
        | "lumber"
        | "wool"
        | "grain"
        | "ore"

dev_card: "knight"
    | "a victory point" -> victory_point
    | "year of plenty"
    | "monopoly"
    | "road building"

special: "longest road"
    | "largest army"
    | "Harbor Master"

dice_digits: /(1[0-2]|[2-9])/

%import common.NUMBER
%import common.WS
%ignore WS
"""


def count_points(action):
    child = str(action)
    if 'build' in child:
        if 'settlement' in child:
            return 1
        elif 'city' in child:
            return 2
    elif 'achieve' in child:
        return 2
    elif 'draw' in child:
        if 'victory_point' in child:
            return 1
    return 0

def getScores(tree):
    '''
    Someone is in the lead if they have the most victory points.
    Someone has won once they have 15 Victory Points
    2 Victory points are given when a player achieves "special"
    Building a settlement awards you 1 Victory Point
    Building a city gets you 2 Victory Points
    '''
    player_names = []
    player_points = []

    for turn in tree.find_data('turn'):
        player_name = str(turn.children[0].children[0])
        if player_name not in player_names:
            player_names.append(player_name)
            player_points.append(0)

        player_index = player_names.index(player_name)
        for action in turn.children[2:]:
            player_points[player_index] += count_points(action)
    return player_points, player_names


def getLeader(tree):
    scores, names = getScores(tree)
    leader_index = scores.index(max(scores))
    return names[leader_index], scores[leader_index]


def getLeaderboard(tree):
    scores, names = getScores(tree)
    combined = list(zip(names, scores))
    sorted_leaderboard = sorted(combined, key=lambda x: x[1], reverse=True)
    return sorted_leaderboard


parser = Lark(catan_grammar, ambiguity='explicit')
parse_tree = parser.parse(game)
standings = getLeaderboard(parse_tree)

max_name_length = max(len(player) for player, _ in standings)

print(f"{('*' * 9)} Leaderboard {('*' * 9)}")
for i, (player, points) in enumerate(standings):
    num_stars = max_name_length - len(player) + 2
    print(
        f"\n{i+1:>{2}}) {player:<{max_name_length}} {('-' * 10)} {points:<{2}} points")
print(f"\n{('*' * 32)}")
winner, points = getLeader(parse_tree)
if (points >= 15):
    print(f'\n{winner} has won by getting {points} Victory Points!\n')
else:
    print(f'\n{winner} is in the lead with {points} points!\n')
