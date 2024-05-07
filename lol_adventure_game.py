from argparse import ArgumentParser
import re
import random
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
        clothing (list): The chacracter's clothing.
    """
    def __init__(self, name):
        """Initializes a character and its features including name, health, money, attack 
        damage, defense, weapons, and the starting round. 
        
        Attributes:
        
        Side effects:
        - Creates and assigns values to the multiple attributes for the character.
        """
        if not re.match(r""""(?x)^[[/a-zA-Z]* \d*\s*[/a-zA-Z]*\d*[/a-zA-Z]*]{1,30}$"gm""", name):
            raise ValueError("Invalid character name. Must only contain letters and spaces, up to 30 characters.")
        self.name = name
        self.health = 100 
        self.money = 50
        self.round = 1
        self.attack_damage = 0
        self.defense = 0
        self.weapon = None
        self.hair_color = None
        self.eye_color = None
        self.clothing = []
        self.shop = None # attribute to hold ref to shop
    
    def __repr__(self):
        """Return a string representation of the Character object

        Returns:
            str: A formatted string containing the character's name, health, and starting money

        Side effects:
            None
        """
        return f"Hello {self.name}! you have {self.health}% health, and {self.money} coins to begin the game."

    def appearance(self):
        """
        Ask the user to customize the character's appearance.
                
        Users can choose hair color, eye color, and clothing items.
        Values will be stored in Character

        Side Effects:
            Creates attributes for hair_color, eye_color, clothing and assign values to them
        
        Raises:
            ValueError: If the user's input for hair or eye color is invalid.
            Prints out statement if clothing choice is invalid
            Prints out character description to console
        """
        clothing_options = ["hat", "shirt", "pants", "shoes"]

        #ask user for hair color
        self.hair_color = input("Enter your hair color: ")

        #ask user for eye color
        self.eye_color = input("Enter your eye color: ")

        #ask user for clothing items
        print("Available clothing options: " + ", ".join(clothing_options))
        while True:
            choice = input("Enter a clothing item (or 'done' to finish): ").lower()
            if choice == "done":
                break
            elif choice in clothing_options:
                self.clothing.append(choice)
            else:
                print("Invalid choice. Please try again.")

        #print character description
        print(f"\nYour character's appearance:\nName: {self.name}\nHair Color: {self.hair_color}\nEye Color: {self.eye_color}\nClothing: {', '.join(self.clothing)}")
    
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
    """A subclass representing a shop where players can buy items."""
    def __init__(self,name):
        """Initializes the shop.

        Args:
            name (str): The name of the shop.

        Side effects:
            Initializes shop attributes.
        """
        super().__init__(name)
        self.items = {"health potion": 10} 
        self.health_potion_count = 3  

    def open_shop(self):
        """Displays a list of available items and their prices."""
        print("Welcome to the shop!")
        print("Available items:")
        for item, price in self.items.items():
            print(f"{item}: {price} coins")
    
    def buy_item(self, item):
        """Buy an item from the shop."""
        cost = self.items.get(item)

        if cost is None:
            print(f"'{item}' is not a valid item.")
            return cost
            
        if super().money >= cost:
        
            if item == "health potion" and self.health_potion_count == 0:
                print("You have reached the health potion limit.")


class Monsters():
    def __init__(self, round, monsters):
        self.round = round
        self.monsters = monsters
        self.default_money = 0
        self.monster_dmg = 10 + (round - 1) * 5
    def questions(self):
        questions_file = f"{self.round}_questions.txt"
        qa_dict = {}
        with open(questions_file, 'r') as file:
            lines = file.readlines()
            # Process each line (question-answer pair)
            for line in lines:
                if line.strip():
                    question, answers = line.strip().split(':')
                    answer_list = [ans.strip() for ans in answers.split('-')]
                    qa_dict[question.strip()] = answer_list
        random_question = random.choice(list(qa_dict.keys()))
        return self.monsters[self.round], {random_question: qa_dict[random_question]}

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
    parser.add_argument("--shop", action="store_true", help="Interact with the shop")

    # more command-line arguments required eventually for the Shop() and Monsters() classes

    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    # to be worked on further as the game develops

    main(args.name, weapon=args.weapon,
         hair_color=args.hair_color, eye_color=args.eye_color)
