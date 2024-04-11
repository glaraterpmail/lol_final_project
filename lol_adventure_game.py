from argparse import ArgumentParser
"""An adventure game that helps a player practice Python concepts by providing 
questions for players to answer in each round of the game to answer to beat the monsters."""

class Character():
    def __init__():
    
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

def parse_args(arglist):
    """ Parse command-line arguments.
    """
    parser = ArgumentParser()
    parser.add_argument()
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
