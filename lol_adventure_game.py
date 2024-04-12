from argparse import ArgumentParser
import re
"""An adventure game that helps a player practice Python concepts by providing 
questions for players to answer in each round of the game to answer to beat the 
monsters."""

class Character():
    """A class representing a character of an adventure game.
    
    Attributes:
        name (str): Name of the character.
        health (int): Current health of the character.
        money (int): Current money of the character.
        round (int): The round the game is on.
        attack_damage(int): How much damage the character deals.
        defense (float): Chance in percentage that the character has to dodge
            an attack if they answer incorrectly.
        weapon (str): The character's weapon.
        hair_color (str): The character's hair color.
        eye_color (str): The character's eye color.
    """
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
        """Return a string representation of the Character object

        Returns:
            str: A formatted string containing the character's name, health, and starting money

        Side effects:
            None
        """
        return f"Hello {self.name}! you have {self.health}% health, and {self.money} coins to begin the game."

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
            - Updates `weapon`, `attack_damage`, and `defense` attributes 
            depending on the chosen weapon.
            - Raises a ValueError if the weapon is not "sword" or "magic".
        """
        if weapon not in ["sword", "magic"]:
            raise ValueError("Invalid weapon! Please choose either 'sword' "
                             "or 'magic'.")
        self.weapon = weapon
        self.attack_damage = 25 if weapon == "sword" else 20
        self.defense = 0.05 if weapon == "sword" else 0.10

class Shop(Character):
    def __init__():

    def open_shop():
    
    def buy_item():

class Monsters():
    def __init__():
    
    def questions():

def game_master():

def parse_args(arglist):
    """ Parse command-line arguments.
   
    Args:
        arglist (list): A list of command-line arguments to be parsed


    Returns:
        Namespace: An object containing the parsed arguments as attributes


    """
    parser = ArgumentParser()
    parser.add_argument("name", type=str, help="Name of the player")
    parser.add_argument("--weapon", choices=["sword", "magic"], help="Weapon choice (optional)")
    parser.add_argument("--hair-color", type=str, help="Hair color choice (optional)")
    parser.add_argument("--eye-color", type=str, help="Eye color choice (optional)")

    # more command-line arguments required eventually for the Shop() and Monsters() classes

    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    # to be worked on further as the game develops

    main(args.name, weapon=args.weapon,
         hair_color=args.hair_color, eye_color=args.eye_color)
