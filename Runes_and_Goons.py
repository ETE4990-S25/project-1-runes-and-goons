#Alexander Land and Maggie Tapia

import random
import math
import json

import os

from game_map import map as map
from game_phases import combat as combat
from game_phases import pickup_items as pickup_items


gameover = False



class player(object):
    """creates player object to store data"""
    def __init__(self, name, health, damage, max_health):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = max_health

    def loader(self, game_data):
        self.health = game_data['player health']


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
            #looks like {equipname: {type: ... , attributes: {damage: ... ,speed: ... } }}
            

    def loader(self, game_data):
        self.weapons_and_spells = game_data['equipment']
        self.healing_potions = game_data['healing potions']


def saver(mapinstance, playerinstance, inventoryinstance):
    game_data = {'map': mapinstance.rooms,
    'current room' : mapinstance.current_room,
    'previous room' : mapinstance.previous_room,
    'equipment': inventoryinstance.weapons_and_spells,
    'healing potions':inventoryinstance.healing_potions,
    'player health': playerinstance.health}
    
    with open('game_data.json', 'w') as json_file:
        json.dump(game_data, json_file, indent=4)

def loader(mapinstance, inventory, playerinstance):
    """loads game data, if it fails it'll raise an exception"""
    game_data = {}
    with open('game_data.json') as file:
        game_data = json.load(file)

    try:
        mapinstance.loadsavedgame(game_data)
        inventory.loader(game_data)
        playerinstance.loader(game_data)
        print('game successfully loaded\n')
        return True
    except:
        print('game did not load\n')
        raise Exception("failed load")




# Start of main code
gameover = False
mapinstance = map()
player_inventory = equipment_inventory()

player_name = str(input("What is your name: "))
playerinstance = player(name= player_name,health= 300,damage= 10, max_health= 300)  


# tries asks if playing from a load file or playing from the default new game file
# the while loop will not break until a succesful load of data
while 1:
    neworloadgame = str(input('Load or New Game:\n1: New Game\n2: Load from save\n'))
    if not(neworloadgame == '2'):
        # fills map with the default enemies and items
        mapinstance.loadnewgame()

        #gives starting weapon with new game
        player_inventory.get_equipment('Rusty Sword','weapon',{'damage': 5, 'speed': 1})

        break
    else:
        try: 
            loader(mapinstance, player_inventory, playerinstance)
            break
        except:
            pass





while not gameover:

    mapinstance.move()

    combat(mapinstance, playerinstance, player_inventory)

    if gameover:
        break

    pickup_items(mapinstance, player_inventory)

    saver(mapinstance, playerinstance, player_inventory)


print('\n\nGAME OVER\n\n')
