#Alexander Land and Maggie Tapia

import random
import math
import json

import os

gameover = False

# todo 
# combat
# add print statements to spells, weapons, and enemies
# player health
# fix spells in rooms dict
# win loss
# player name code



#room handling
class map(object):
    """creates a map of the game
    contains every item and enemy in every room. 
    the data will be saved in the self.rooms dictionary"""
    def __init__(self):
        self.rooms = {}

    def loadsavedgame(self):
        global game_data
        self.rooms = game_data['map']
        self.current_room = game_data['current room']
        self.previous_room = game_data['previous room']

    def loadnewgame(self):
        self.rooms = {'Starting Room': {'East': 'The Drowned Gate', #Home of the Game
                                        'South': 'The Embered Threshold',
                                        'West': 'Ancient Convergence'
                                        },
                                        

                    'The Embered Threshold': {'North': 'Starting Room', #Fire Area
                                            'East': 'Smoldering Ascent',
                                            'South': 'Magma Crucible',
                                            'West': 'Stormfire Bastion',
                                            'Item': {'name': 'Fireball',
                                                     'damage': 5,
                                                     'element': 'fire',
                                                     'type': 'spell'},
                                            'Enemy': {'name': 'Goblin',
                                                  'health': 15,
                                                    'weakness': 'water',
                                                    'damage': 3,
                                                    'speed': 2,
                                                    'speech': 'Oh, you actually think you stand a chance? Cute. Now, lets see if you can dodge *this!*'},
                                            'healing potion': 2,
                                                    },

                    'Stormfire Bastion': {'East': 'The Embered Threshold',
                                        'Item': {'name':'Blazing Maelstrom',
                                                 'damage': 10,
                                                 'speed': 2,
                                                 'type': 'weapon'},
                                        'Enemy': {'name': 'Fire Elemental',
                                                  'health': 75,
                                                  'weakness': 'water',
                                                  'damage': 7,
                                                  'speed': 2,
                                                  'speech': 'You dare to challenge me? You will be reduced to ashes!'},
                                        'healing potion': 1,
                                        },

                    'Magma Crucible': {'North': 'The Embered Threshold',
                                        'Item': {'name':'Volcanic Maul',
                                                'damage': 15,
                                                 'speed': 2,
                                                 'type': 'weapon'},
                                        'Enemy': {'name': 'Lava Golem',
                                                  'health': 120,
                                                  'weakness': 'water',
                                                  'damage': 12,
                                                  'speed': 1,
                                                  'speech': 'You are not worthy to face me! Prepare to be melted down!'},
                                        'healing potion': 2,
                                        },

                    'Smoldering Ascent': {'West': 'The Embered Threshold',
                                        'Item': {'name':'Inferno Fang',
                                                 'damage': 18,
                                                 'speed': 2,
                                                 'type': 'weapon'},
                                        'Enemy': {'name': 'Fire Dragon',
                                                  'health': 180,
                                                  'weakness': 'water',
                                                  'damage': 15,
                                                  'speed': 2,
                                                  'speech': 'You are brave to face me, but you will be reduced to ashes!'},
                                        'healing potion': 2,
                                        },

                    'The Drowned Gate': {'West': 'Starting Room', #Water Area
                                        'South': 'Frozen Depths',
                                        'East': 'Whirlpool Shrine',
                                        'North': 'Abyssal Cavern',
                                        'Item': {'name':'Water Blast',
                                                    'damage': 5,
                                                    'element': 'water',
                                                    'type': 'spell'},
                                        'Enemy': {'name': 'Mermaid',
                                                  'health': 15,
                                                  'weakness': 'fire',
                                                  'damage': 3,
                                                  'speed': 2,
                                                  'speech': 'You dare to challenge me? You will be drowned!'},
                                        'healing potion': 1,
                                                                    },
                                                

                    'Abyssal Cavern': {'South': 'The Drowned Gate',
                                    'Item': {'name':'Abyssal Trident',
                                             'damage': 12,
                                             'speed': 2,
                                             'type': 'weapon'},
                                    'Enemy': {'name': 'Siren',
                                              'health': 90,
                                              'weakness': 'fire',
                                              'damage': 6,
                                              'speed': 2,
                                              'speech': 'You are not worthy to face me! Prepare to be drowned!',
                                              },
                                    'healing potion': 2,
                                    },

                    'Frozen Depths': {'North': 'The Drowned Gate',
                                    'Item': {'name':'Glacier Fang',
                                             'damage': 15,
                                             'speed': 2,
                                             'type': 'weapon'},
                                    'Enemy': {'name': 'Ice Golem',
                                              'health': 140,
                                              'weakness': 'fire',
                                              'damage': 9,
                                              'speed': 1,
                                              'speech': 'You are brave to face me, but you will be frozen solid!'},
                                    'healing potion': 1,
                                    },

                    'Whirlpool Shrine': {'West': 'The Drowned Gate',
                                        'Item': {'name':'Whirlpool Staff',
                                                 'damage': 16,
                                                 'speed': 3,
                                                 'type': 'weapon'},
                                        'Enemy': {'name': 'Water Elemental',
                                                  'health': 170,
                                                  'weakness': 'fire',
                                                  'damage': 15,
                                                  'speed': 2,
                                                  'speech': 'You are brave to face me, but you will be drowned!'},
                                        'healing potion': 2,
                                        },

                    'Ancient Convergence': {'East': 'Starting Room',
                                            'Enemy': {'name': 'Ancient Guardian',
                                                      'health': 600,
                                                      'weakness': 'none',
                                                      'damage': 25,
                                                      'speed': 2,
                                                      'speech': 'You have come far, but you will not pass!'},
                                            'healing potion': 3,
                                                      },
                      #end of game area, final boss
                    }
        self.current_room = 'Starting Room'
        self.previous_room = 'Starting Room'



def move():
    """when called it'll ask the player which room they want to move to and allow them to move there
    Also doesn't allow illegal movement"""
    directions = ["North", "South", "East", "West"]

    while True:
        print(f"You're in the {mapinstance.current_room}")

        print(f"These are the rooms connected to the room you're in: \n")


        for (nav, room) in mapinstance.rooms[mapinstance.current_room].items():
            if nav in directions:
                print(f"{nav}: {room}")

        desired_direction = str(input("\ntype the direction you want to move: ")).title()

        if desired_direction in directions and desired_direction in mapinstance.rooms[mapinstance.current_room]:
            mapinstance.previous_room = mapinstance.current_room
            mapinstance.current_room = mapinstance.rooms[mapinstance.current_room][desired_direction]
            print("-"*50)
            print(f"\n\nYou walk into: {mapinstance.current_room}")

            break
        else:
            print("\nThere is no room in that direction \nPlease type a valid direction")
            print("------------------------------------------------------------------------------------\n")

class player(object):
    """creates player object to store data"""
    def __init__(self, name, health, damage, max_health):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = max_health

    def loader(self):
        self.health = game_data['player health']

class enemy(object):
    """creates enemy and manages damage from enemies"""
    def __init__(self,name,health,weakness,damage,speed,speech=None):
        self.name = name
        self.health = health
        self.weakness = weakness
        self.damage = damage
        self.speed = speed
        self.speech = speech
           
    def attack(self,player):
        """attacks player, speed calculations will be done elsewhere"""
        player.health -= self.damage
        print(f"{self.name} did {self.damage} damage to you")

    def speak(self):
        """prints the saved line that the creature would say"""
        print("\"", self.speech,"\"")

class weapons(object):
    """creates weapon for warrior"""
    def __init__(self, name, damage, speed):
        self.name = name
        self.damage = damage
        self.speed = speed

    def attack(self, enemy):
        enemy.health -= self.damage

        print(f'{self.name} did {self.damage} damage')
        
        speed_diff = self.speed - enemy.speed
        if speed_diff > 0:
            probability_of_second_hit = 1 / (1 + math.exp((3-speed_diff)))
            if probability_of_second_hit*100 > random.randint(1,100):
                enemy.health -= self.damage
                print(f'{self.name} did {self.damage} damage again because of speed advantage')
        # if speed difference is great enough the weapon has a chance to hit twice.

class spells(object):
    """Creates spells for wizard
    spells have a damage value and an element"""
    def __init__(self,name,damage,element):
        self.name = name
        self.damage = damage
        self.element = element

    def attack(self, enemy):
        """deals damage to enemy depending on elemental weakness"""
        if self.element == enemy.weakness:
            enemy.health -= self.damage*1.5
            print(f'ELEMENTAL CRIT!!')
            print(f'{self.name} did {self.damage*1.5} damage')
        else:
            enemy.health -= self.damage
            print(f'{self.name} did {self.damage} damage')


class equipment_inventory(object):
    """spells and weapons are equipment for attacking
    this class will handle which equipment the player has and using the weapons"""
    def __init__(self):
        self.weapons_and_spells = {}
        self.duplicate_item = False
        self.healing_potions = 0


    def get_equipment(self, equipment_name, type, attributes = None):
        """adds equiment based on type"""

        self.duplicate_item = False

        for entry in self.weapons_and_spells:
            if entry == str(equipment_name):
                print(f'you got a {equipment_name} but you already had one so it was thrown away.')
                self.duplicate_item = True
    
        if not self.duplicate_item:
            self.weapons_and_spells[equipment_name]={'type':type, 'attributes': attributes}
            #looks like {equipname:{type:,attributes:{damage:,speed:}}}
            
    def useHealPotion(self):
        if self.healing_potions >= 1:
            self.healing_potions -= 1
            playerinstance.health = playerinstance.max_health
            print(f'\nYou have {self.healing_potions} remaining\n Health restored to {playerinstance.max_health}\n')
        else: 
            print(f"\nNo health potions remaining... :(\n")

    def loader(self):
        self.weapons_and_spells = game_data['equipment']
        self.healing_potions = game_data['healing potions']

def pickup_items():
    """after ending up in a room run pickup items to allow """

    if not('Item' in mapinstance.rooms[mapinstance.current_room] or 'healing potion' in mapinstance.rooms[mapinstance.current_room]):
            print("\nThere is no item in the room.")
            print("-" * 50)
            

    if 'Item' in mapinstance.rooms[mapinstance.current_room]:
        print(f"\n You found a {mapinstance.rooms[mapinstance.current_room]['Item']['name']}!")
        print("Do you want to pick it up? (y/n)")
        pickup = str(input()).lower()
        if pickup == 'y':
            item_name = mapinstance.rooms[mapinstance.current_room]['Item']['name'] 
            item_type = mapinstance.rooms[mapinstance.current_room]['Item']['type']

            if item_type == 'weapon':
                item_attributes = {'damage':mapinstance.rooms[mapinstance.current_room]['Item']['damage'],
                                    'speed':mapinstance.rooms[mapinstance.current_room]['Item']['speed']}
            elif item_type == 'spell':
                item_attributes = {'damage':mapinstance.rooms[mapinstance.current_room]['Item']['damage'],
                                     'element':mapinstance.rooms[mapinstance.current_room]['Item']['element']}
            else:
                pass

            player_inventory.get_equipment(item_name,item_type, item_attributes)

            print(f"You picked up the {item_name}!")
            print("-" * 50)
            del mapinstance.rooms[mapinstance.current_room]['Item']

        else:
            print(f"You left the {mapinstance.rooms[mapinstance.current_room] ['Item']['name']} behind.")
            print("-" * 50)

    if 'healing potion' in mapinstance.rooms[mapinstance.current_room]: 
        player_inventory.healing_potions += mapinstance.rooms[mapinstance.current_room]['healing potion']
        print(f'you found {mapinstance.rooms[mapinstance.current_room]['healing potion']} healing potions!')
        del mapinstance.rooms[mapinstance.current_room]['healing potion']
    



def combat():
    global gameover

    if "Enemy" in mapinstance.rooms[mapinstance.current_room]:
        current_enemy = enemy(mapinstance.rooms[mapinstance.current_room]["Enemy"]["name"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["health"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["weakness"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["damage"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["speed"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["speech"])

        print(f"\nA {current_enemy.name} appeared!!\n")

        print(f"{current_enemy.name}'s stats\n---------------------")
        print(f"health: {current_enemy.health}\ndamage: {current_enemy.damage}\nweakness: {current_enemy.weakness}\nspeed: {current_enemy.speed}\n")

        print(f"You\'re health is currently at: {playerinstance.health} ({100*playerinstance.health/playerinstance.max_health}%)")

        FightorFlee = input("Do you want to fight or run?\nf: fight\nr: run\n")

        if FightorFlee == 'f':
            """fight code"""
            fighting = True

            print("")
            current_enemy.speak()
            print("")
                            
            while fighting:
                Selecting_Item = True

                while Selecting_Item:
                    #"selecting item or weapon"
                    AttackorUsePotion = input(f"Would you like to:\n1: Attack\n2: Use Health Potion ({player_inventory.healing_potions} remaining)\n")

                    if AttackorUsePotion == "2":
                        player_inventory.useHealPotion()
                    else:
                        #"""attack is chosen and handling attack"""
                        print(f'\n Available Weapons and Spells:')

                        #listing the names of weapons and spells and their values
                        for name_weaponspell, weaponspells_dict in player_inventory.weapons_and_spells.items():
                            print(f'{name_weaponspell}: {weaponspells_dict['attributes']}')

                        while True: #checking for valid attack
                            selected_attack = str(input("\ntype name of weapon or spell: ")).title()
                            print("")

                            if selected_attack not in player_inventory.weapons_and_spells:
                                print('Please type valid weapon or spell\n')
                            else:
                                if player_inventory.weapons_and_spells[selected_attack]['type'] == 'weapon':
                                    # extremely long function instanciating weapon with values from inventory
                                    # the spells version is the sambe but it instanciates element
                                    current_attack = weapons(selected_attack,
                                                             player_inventory.weapons_and_spells[selected_attack]['attributes']['damage'],
                                                             player_inventory.weapons_and_spells[selected_attack]['attributes']['speed'])
                                    
                                else:
                                    current_attack = spells(selected_attack,
                                                             player_inventory.weapons_and_spells[selected_attack]['attributes']['damage'],
                                                             player_inventory.weapons_and_spells[selected_attack]['attributes']['element'])
                                #finally does the attack after all the menuing
                                current_attack.attack(current_enemy)
                                print(f"{current_enemy.name} has {current_enemy.health} health remaining\n")
                                break

                        Selecting_Item = False

                #after attacking enemy
                if current_enemy.health <= 0:
                    #check if enemy is killed then leave combat
                    print(f"{current_enemy.name} killed")
                    print("-"*50)
                    del mapinstance.rooms[mapinstance.current_room]['Enemy']
                    fighting = False
                    break
                
                #enemy attacks back
                current_enemy.attack(playerinstance)
                print(f"You have {playerinstance.health} health\n")

                if playerinstance.health <= 0:
                    #player died

                    print(f"you died to {current_enemy.name}")
                    gameover = True
                    fighting = False

        else:
            """flee code"""
            mapinstance.current_room = mapinstance.previous_room
            print(f'\nYou\'ve fled to the previous room\nCurrent Room: {mapinstance.current_room}')
            return
        

    else:
        print(f"There's no enemy in this room")
               


def saver():
    game_data = {'map': mapinstance.rooms,
    'current room' : mapinstance.current_room,
    'previous room' : mapinstance.previous_room,
    'equipment': player_inventory.weapons_and_spells,
    'healing potions':player_inventory.healing_potions,
    'player health': playerinstance.health}
    with open('game_data.json', 'w') as json_file:
        json.dump(game_data, json_file, indent=4)

def loader():
    global game_data
    with open('game_data.json') as file:
        game_data = json.load(file)
        print(game_data)




# Start of main code
game_data = {}
gameover = False
mapinstance = map()
player_inventory = equipment_inventory()

player_inventory.get_equipment('Rusty Sword','weapon',{'damage': 5, 'speed': 1})

player_name = str(input("What is your name: "))
playerinstance = player(name= player_name,health= 300,damage= 10, max_health= 300)  

while 1:
    neworloadgame = str(input('Load or New Game:\n1: New Game\n2: Load from save\n'))
    if not(neworloadgame == '2'):
        mapinstance.loadnewgame()
        break
    else:
        try:
            loader()
            mapinstance.loadsavedgame()
            player_inventory.loader()
            playerinstance.loader()
            print('game successfully loaded\n')
            break
        except:
            print('game did not load\n')



while not gameover:
    move()
    combat()
    if gameover:
        break
    pickup_items()
    saver()


print('\n\nGAME OVER\n\n')
