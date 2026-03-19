# Advanced Dice Game 🎲

A strategic dice game based on classic rules where players compete for the highest score by filling different scoring categories.

## How to Play

1. Run the game using Python: `python dice_game.py`
2. Choose number of rounds (or 0 for unlimited play until all categories are filled)
3. Enter number of players (1-4) and their names
4. Each player takes turns rolling 5 dice and scoring points

## Game Rules

### Gameplay
- Each turn, you roll 5 dice up to 3 times
- After each roll (except the last), you can choose which dice to re-roll
- You can also "resign" after the 2nd or 3rd roll to keep current dice
- After your throws, you must assign the result to one unused category
- If the result doesn't fit any category, you must pick a category and score 0

### Scoring Categories

**Number Categories (1-6):**
- Sum all dice showing that number (e.g., three 4s = 12 points in Fours)

**Combination Categories:**
- **Pair:** Sum of the highest pair (e.g., two 4s = 8 points)
- **Two Pairs:** Sum of both pairs (e.g., two 4s + two 6s = 20 points). Four of a kind also counts as two pairs.
- **Three of a Kind:** Sum of three identical dice (e.g., three 4s = 12 points). Four of a kind also counts.
- **Four of a Kind:** Sum of four identical dice (e.g., four 4s = 16 points)
- **Poker (5 of a Kind):** Sum of all five dice (e.g., five 4s = 20 points)
- **Full House:** Pair + Three of a Kind (e.g., three 4s + two 6s = 24 points)
- **Low Straight:** 1-2-3-4-5 sequence (always 15 points)
- **High Straight:** 2-3-4-5-6 sequence (always 20 points)
- **Chance:** Sum of all five dice (any combination)

## Features

- Support for 1-4 players
- Configurable number of rounds or unlimited play
- Strategic dice selection and re-rolling
- Complete scoring system with all standard categories
- Interactive scoreboard showing all player progress
- Visual dice display
- Turn-based gameplay with clear instructions

## Requirements

- Python 3.x
- No external dependencies (uses only built-in modules)

## Running the Game

```bash
python dice_game.py
```

## Strategy Tips

- Plan ahead which categories you might want to fill
- Sometimes it's better to take 0 points in a low-value category to save a high-value one
- Pay attention to what categories your opponents are filling
- The "resign" option can be useful when you have a good combination early

Enjoy playing this strategic dice game! 🎲
