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
        if weapon not in ["sword", "magic"]:
            raise ValueError(""Invalid weapon! Please choose either "sword" or /
                             "magic"."")

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
