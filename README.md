# lol_final_project
An adventure game that helps a player practice Python concept by providing questions for players to answer in each round of the game to answer to beat the monsters.

## Files:
- **lol_adventure_game.py:** a python file containing the code that runs the game
- **1_questions.txt:** a txt file containing questions about container data types for the first round of the game
- **2_questions.txt:** a txt file containing questions about inheritance and composition for the second round of the game
- **3_questions.txt:** a txt file containing questions about regular expressions for the third round of the game
- **4_questions.txt:** a txt file containing questions about magic methods for the fourth round of the game
- **5_questions.txt:** a txt file containing questions about pandas and dataframs for the fifth round of the game

## Instructions:
**How to run the program:**
- From the command line, enter "python3 lol_adventure_game.py"
- Windows users, type "python" instead of "python3" when you run your program.
**How to interpret results:**
- The game will start of by asking for the characteristics of your character.
- After entering your characteristics and choosing your weapon, the game rounds will begin.
- There will be 5 rounds and for each round, you will have to answer questions about Python.
- You will lose health everytime you answer a question wrong and if your health reaches 0, the game will end and you lose.
- If you answer all 5 questions correctly, the game will end and you win.

## Table:
| Method/function       | Primary author | Techniques demonstrated            |
|:---------------------:|:--------------:|:----------------------------------:|
| Character.__init__    | Elenna Mach    | regular expressions                |
| Character.__repr__    | Gabrielle Lara | magic method                       |
| Character.appearance  | Steven Nguyen  | f-strings containing expressions   |
| Character.pick_weapon | Nhi Pham       | conditional expressions            |
| Shop.__init__         | Steven Nguyen  | super()                            |
| Shop.open_shop        | Gabrielle Lara |                                    |
| Shop.buy_item         | Steven Nguyen  |                                    |
| Monsters.__init__     | Elenna Mach    |                                    |
| Monsters.questions    | Elenna Mach    | with statements                    |
| game_master           | Nhi Pham       | set operations on sets             |
| parse_args            | Gabrielle Lara | ArgumentParser class from argparse |