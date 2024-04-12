from argparse import ArgumentParser
import re
"""An adventure game that helps a player practice Python concepts by providing 
questions for players to answer in each round of the game to answer to beat the monsters."""

class Character():
    def __init__(self, name):
        """Initializes a character and its features including name, health, money, attack 
        damage, defense, weapons, and the starting round. 
        
        Attributes:
        
        Side effects:
        - Creates and assigns values to the multiple attributes for the character.
        """
        # not finished regular expression
        if not re.match(r""""(?x)^[[/a-zA-Z]* \d*\s*[/a-zA-Z]*\d*[/a-zA-Z]*]{1,30}$"gm""", name):
            raise ValueError("Invalid character name. Must only contain letters and spaces, up to 30 characters.")
        self.name = name
        self.health = 100 
        self.money = 50
        self.round = 1
        self.attack_damage = 0
        self.defense = 0
        self.weapon = None
    
    def __repr__():

    def appearance():
        clothing_options = ["hat", "shirt", "pants", "shoes"]
        self.hair_color = input("Enter your hair color: ")
        self.eye_color = input("Enter your eye color: ")
        print("Available clothing options: " + ", ".join(clothing_options))
        while True:
            choice = input("Enter a clothing item (or 'done' to finish): ").lower()
    
    def pick_weapon(self, weapon):
        """Pick a weapon for the character.

        Args:
            weapon (str): The weapon of choice (either "sword" or "magic").

        Raises:
            ValueError: If the provided weapon is not "sword" or "magic".
            
        Side effects:
            - Updates `weapon`, `attack_dmg`, and `defense` attributes 
            depending on the chosen weapon.
            - Raises a ValueError if the weapon is not "sword" or "magic".
        """
        if weapon not in ["sword", "magic"]:
            raise ValueError("Invalid weapon! Please choose either 'sword' "
                             "or 'magic'.")
        self.weapon = weapon
        self.attack_dmg = 25 if weapon == "sword" else 20
        self.defense = 0.05 if weapon == "sword" else 0.10

class Shop(Character):
    def __init__():

    def open_shop():
    
    def buy_item():

class Monsters():
    def __init__():
    
    def questions():

def game_master():

<<<<<<< HEAD
def parse_args(arglist):
=======
def parse_args(arglist):
    """ Parse command-line arguments.
    """
    parser = ArgumentParser()
    parser.add_argument()
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
>>>>>>> 09c1be8b4ec76252b70ee81bddb7c6ec5bac48a4
