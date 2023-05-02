# CatanLittleLanguage Formatting

This file provides information on how to format phrases for the CatanLittleLanguage. Use this guide when writing game sequences to ensure that the parser can properly understand your input.

## Game Initialization
- Start a game with a list of players: `start game [player1, player2, player3, ...]`

## Turns
- Player rolls dice: `[player] rolls [number]`
- Player ends turn: `(newline)`

## Actions
- Draw a development card: `[player] draws [development card] development card`
- Build a structure: `[player] builds [structure] at {[x,y]}`
- Trade resources: `[player] trades [resource list] with [other player] for [resource list]`
- Use a development card: `[player] uses [development card] card`
- Achieve a special: `[player] gets [special] achievement`

### Development Cards
- Knight: `knight`
- Victory Point: `a victory point`
- Year of Plenty: `year of plenty`
- Monopoly: `monopoly`
- Road Building: `road building`

### Structures
- Road: `road`
- City: `city`
- Settlement: `settlement`

### Resources
- Brick: `brick`
- Lumber: `lumber`
- Wool: `wool`
- Grain: `grain`
- Ore: `ore`

### Specials
- Longest Road: `longest road`
- Largest Army: `largest army`
- Harbor Master: `Harbor Master`

## Example Turn with Multiple Actions
start game Willy, John, Sarah, and Ben
Willy rolls 9
John rolls 7 and builds road at {4,2}
Sarah rolls 4
Ben rolls 8 and draws knight development card
Willy rolls 5 and trades 2 ore with Sarah for 1 brick, 2 grain, and 2 wool
John rolls 2
Sarah rolls 8 and builds settlement at {10,22} and builds road at {10,22}
Ben rolls 4 and trades 4 ore with John for 1 wool, 2 grain, and 1 lumber
