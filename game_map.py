import json


class map(object):
    """creates a map of the game
    contains every item and enemy in every room. 
    the data will be saved in the self.rooms dictionary
    
    all other game functions will interact with this dictionary to update current state of the game """

    def __init__(self):
        self.rooms = {}

    def move(self):
        """when called it'll ask the player which room they want to move to and allow them to move there
        Also doesn't allow illegal movement"""
        directions = ["North", "South", "East", "West"]

        while True:
            print(f"You're in the {self.current_room}")

            print(f"These are the rooms connected to the room you're in: \n")


            for (nav, room) in self.rooms[self.current_room].items():
                if nav in directions:
                    print(f"{nav}: {room}")

            desired_direction = str(input("\ntype the direction you want to move: ")).title()

            if desired_direction in directions and desired_direction in self.rooms[self.current_room]:
                self.previous_room = self.current_room
                self.current_room = self.rooms[self.current_room][desired_direction]
                print("-"*50)
                print(f"\n\nYou walk into: {self.current_room}")

                break
            else:
                print(("-"*50)+"\n")
                print("\nThere is no room in that direction \nPlease type a valid direction \n")
 

    def loadsavedgame(self, game_data):
        """fills the map with data from the save file"""

        self.rooms = game_data['map']
        self.current_room = game_data['current room']
        self.previous_room = game_data['previous room']

    def loadnewgame(self):
        with open('newgamemap.json') as file:
            self.rooms = json.load(file)

        self.current_room = 'Starting Room'
        self.previous_room = 'Starting Room'
