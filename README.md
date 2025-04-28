# Runes and Goons 

In this adventure game, you’ll explore a world made up of different connected rooms. 
Each room can have potions, powerful weapons, or even dangerous bosses waiting for you. 
Your goal? Survive, collect cool items, and defeat all the bosses—including the final one—to beat the game. 

### Definitions and How to Play:

#### Start of Game
You begin in the Start room. 
From here, you can move north, south, east, or west 
depending on which rooms are connected.

#### Navigating Each Room
Every room is part of a bigger world. 
Some rooms are safe and have helpful things like potions 
(which heal you) or weapons (which make you stronger). 
Other rooms have bosses you’ll need to defeat.

#### Items (Weapons and Potions)
Potions heal you during battles, and you can more after battles. Some rooms give you 1, 2, 
or even 3 potions, so grab them when you can!

If a room has a weapon, you can pick it up and use it in battles. 
Each one has a name, like “Volcanic Maw” or “Abyssal Trident.”

#### Bosses and Defeating them
Boss rooms are marked clearly (like Stormfire Bastion or Frozen Depths). You can either:
- Fight the boss and move forward
- Or flee, explore other rooms to collect more potions or weapons, and come back stronger

Once all boss rooms have been completed, you’ll be strong enough for the final challenge. Beat the final boss to win the game!


## Table of Contents

### Main Game file
    - Runes_and_Goons.py

### Sub Game Files

    - game_map.py
       
    handles movement and map funtions

    - game_phases.py

    Classes and functions related to the combat phases of the game along with the ability to pick up items. 

### Saved Game File
    - game_data.json

### Default Map File
    - newgamemap.json


## How to Run the Game

    1. Ensure you have Python installed on your system.
    2. Clone this repository or download the project files.
    3. Navigate to the project directory in your terminal.
    4. Run the game using the command:
        ```bash
        python Runes_and_Goons.py
        ```


## Map Details

### Map:
    
                         Ancient Convergence: Final Boss Room
                    
                                           /\  
                                           |  
                                           |   
                                       Start Room
                                     /\          /\
                                     |            |
                                     |            |
                                     \/           \/
                          The Embered         The Drowned 
                          Threshold           Gate (Water Side)
                          (Fire Side)                       /\
                         /\                                 |
                          |                                 |
                          |                                 |
                        / | \                             / | \
                      /   |   \                         /   |   \
                    /     |     \                     /     |     \
                   \/     |      \/                 \/      |      \/
             Stormfire    |      Smoldering     Abyssal     |     Whirlpool      
              Bastion     |        Ascent       Cavern      |       Shrine  
                         \/                                 \/
                      Magma Crucible                    Frozen Depths

