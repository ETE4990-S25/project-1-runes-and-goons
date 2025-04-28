# holds the functions for combat and picking up items in a room after combat
import math
import random

#classes
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
    """creates weapons
    weapons have a unique speed value when attacking"""
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
    """Creates spells
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


#functions
def useHealPotion(inventoryinstance, playerinstance):
    if inventoryinstance.healing_potions >= 1:
        inventoryinstance.healing_potions -= 1
        playerinstance.health = playerinstance.max_health
        print(f'\nYou have {inventoryinstance.healing_potions} remaining\n Health restored to {playerinstance.max_health}\n')
    else: 
        print(f"\nNo health potions remaining... :(\n")






def combat(mapinstance, playerinstance, inventoryinstance):
    """combat relies on an instance of map, player, equipment_inventory, and the weapons and spells classes
    
    combat will run through the following checks and prompts
    - if enemy in current room it'll do the following:
        - instanciate data from the map as the current_enemy
        - print some data on the enemy
        - ask if player wants to fight or flee
            - if fight it'll let u pick weapons and take turns hitting the enemy
            - if flee it'll return you to the previous room
    - if there is no enemy it'll print that there is nothing and end the combat phase"""
    global gameover

    # if there's an enemy in the rrom it'll instanciate the enemy as the current_enemy
    # Then it'll run through combat with the enemy, otherwise it will just say there is no enemy to fight
    if "Enemy" in mapinstance.rooms[mapinstance.current_room]:
        current_enemy = enemy(mapinstance.rooms[mapinstance.current_room]["Enemy"]["name"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["health"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["weakness"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["damage"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["speed"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["speech"])

        # introducing enemy to player
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
                    # selecting item or weapon
                    # players will be able to choose to heal or attack on each loop
                    # healing doesn't take up the player action so they won't be attacked for healing

                    AttackorUsePotion = input(f"Would you like to:\n1: Attack\n2: Use Health Potion ({inventoryinstance.healing_potions} remaining)\n")

                    if AttackorUsePotion == "2":
                        useHealPotion(inventoryinstance, playerinstance)
                    else:
                        #"""attack is chosen and handling attack"""
                        print(f'\n Available Weapons and Spells:')

                        #listing the names of weapons and spells and their values
                        for name_weaponspell, weaponspells_dict in inventoryinstance.weapons_and_spells.items():
                            #print(f'{name_weaponspell}: {weaponspells_dict['attributes']}')
                            print(f'{name_weaponspell}:')
                            for attribute in weaponspells_dict['attributes']:
                                print(f"    {attribute}: {weaponspells_dict['attributes'][attribute]}")

                        while True: #checking for valid attack
                            selected_attack = str(input("\ntype name of weapon or spell: ")).title()
                            print("")

                            if selected_attack not in inventoryinstance.weapons_and_spells:
                                print('Please type valid weapon or spell\n')
                            else:
                                if inventoryinstance.weapons_and_spells[selected_attack]['type'] == 'weapon':
                                    # instanciating weapon with values from inventory
                                    # the spells version is the same but it instanciates element instead of speed
                                    current_attack = weapons(selected_attack,
                                                             inventoryinstance.weapons_and_spells[selected_attack]['attributes']['damage'],
                                                             inventoryinstance.weapons_and_spells[selected_attack]['attributes']['speed'])
                                    
                                else:
                                    current_attack = spells(selected_attack,
                                                             inventoryinstance.weapons_and_spells[selected_attack]['attributes']['damage'],
                                                             inventoryinstance.weapons_and_spells[selected_attack]['attributes']['element'])
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



def pickup_items(mapinstance, inventoryinstance):
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

            inventoryinstance.get_equipment(item_name,item_type, item_attributes)

            print(f"You picked up the {item_name}!")
            print("-" * 50)
            del mapinstance.rooms[mapinstance.current_room]['Item']

        else:
            print(f"You left the {mapinstance.rooms[mapinstance.current_room] ['Item']['name']} behind.")
            print("-" * 50)

    if 'healing potion' in mapinstance.rooms[mapinstance.current_room]: 
        inventoryinstance.healing_potions += mapinstance.rooms[mapinstance.current_room]['healing potion']
        print(f'you found {mapinstance.rooms[mapinstance.current_room]['healing potion']} healing potions!')
        del mapinstance.rooms[mapinstance.current_room]['healing potion']
    
