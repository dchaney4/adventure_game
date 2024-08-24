import os
import time

from item import *
from player import *
from functions import *
from threat import *
from area import *



######Need to add a search input to global commands
######Need to add a nearby_items function
######add ticking_clock function in
######add look command to global


#initialize main character
main_character = Player()

#initialize items
bandage = Bandage()
magic_mushroom = Magic_Mushroom()
bear = Bear()
club = Club()
bear_spray = BearSpray()

#initilize areas
def no_items_left(area):
    return len(area.nearby_items) == 0

def no_threats_left(area):
    return len(area.nearby_threats) == 0

south_trail = Area('The trail is narrow and winding with dense brush on each side.\nYou notice some colorful fungi growing at the base of an old oak tree.',
                    'The trail is narrow and winding with dense brush on each side.',
                    nearby_items=[(magic_mushroom, 3)],
                    trigger_condition = no_items_left)

north_trail = Area('The trail is narrow and winding with dense brush on each side.\nThere is a large knobby branch lying to the side.',
                    'The trail is narrow and winding with dense brush on each side.',
                    nearby_items=[(club, 1)],
                    trigger_condition = no_items_left)
                    
bear_cave = Area("The dark cave is formed into the base of the mountain, impossible to tell how deep it is..\nA large brown bear guards the entrance while enjoying a meal of fresh salmon.",
                 "The dark cave is formed into the base of the mountain, impossible to tell how deep it is..",
                 nearby_threats = bear,
                 trigger_condition = no_threats_left)

river_area = Area("Large rocks cover the ground across a large, mostly dry river bed.\nYou see a bright red object among the rocks.\nUpon closer inspection, you find the remains of a hiker clad in ruined hiking gear. However a can of bear spray and bandages lie discarded nearby..",
                 "Large rocks cover the ground across a large, mostly dry river bed.\nThe corpse of the hiker and their ruined gear, lay forgotten in the stream..",
                 nearby_items=[(bear_spray, 1), (bandage, 3)],
                 trigger_condition = no_items_left)

bear_cave_interior_area = Area("There is nothing interesting about this cave.. yet",
                               "There is nothing interesting about this cave.. yet",
                               nearby_items= None,
                               trigger_condition = no_items_left)                              


#########~~Input function and commands~#########

#input with unique actions and error codes
def get_input(valid_actions, error_message = "Invalid command.. Type 'help' for a list of commands."):
    global_commands = { 
        'quit': quit_game,
        'help': show_help,
        'status': show_status,
        'inventory': show_inventory,
        'search': search_area,
        
    }
    while True:
        action = input('>').lower() #convert to lowercase
    
        if action in global_commands: #check global commands first
            global_commands[action]()

        elif action == 'use':
            print("Use what?")

        elif action == 'inspect':
            print("Inspect what?")

        elif action == 'equip':
            print("Equip what?")

        elif action == 'pick up':
            print("Pick up what?")
    
        elif action.startswith("use "): #use item input
            item_name = action[4:] #remove use
            main_character.use_item(item_name)

        elif action.startswith("inspect "): #inspect item input
            item_name = action[8:] #remove inspect
            main_character.inspect_item(item_name)

        elif action.startswith("equip "): #equip weapon input
            item_name = action[6:] #remove equip
            main_character.equip_weapon(item_name)

        elif action.startswith("pick up "):#pick up item from area
            item_name = action[8:]#remove pick up
            main_character.pickup_item(item_name)

        #check instance specific valid_actions
        elif action in valid_actions:
            return action

        #print custom error message or default
        else:
            print(error_message)


        continue

#quit input
def quit_game():
    print_slow("Quitting the game...")
    time.sleep(2)
    sys.exit()

#print help screen input
def show_help():
    print("\n(Available commands: quit, help, status, inventory, search, pick up {item name}, use {item name}, inspect {item name}, equip {weapon name})")
    print("Other commands vary based on situation..")

#print player status input
def show_status():
    print(main_character.player_status())

#show inventory input
def show_inventory():
    equipped_weapon = main_character.equipped_weapon.name if main_character.equipped_weapon else 'None'
    inventory_str = ', '.join(f"{item.name} (x{item.quantity})" for item in main_character.inventory) if main_character.inventory else 'Empty'
    print(f"Equipped weapon: {equipped_weapon}")
    print(f"Inventory: {inventory_str}")

def search_area():
    if main_character.current_area is None:
        print_slow("Nothing else to be found.")
    else:
        if not main_character.current_area.nearby_threats:  
            print_slow(main_character.current_area.get_description())
        else:
            print_fast(f"Eliminate all threats first.")

def move_player(area_name):
    main_character.current_area = area_name
    main_character.ticking_clock()

def river_scene():
    scene = '''
      /\\    /\\          /\\
     /  \\  /  \\ /\\     /  \\
    /    \\/        \\  /    \\
   /     /\\         \\/      \\
  /     /  \\     /\\  \\       \\
 /     /    \\   /  \\  \\       \\
/     /      \\ /    \\  \\       \\
     /        \\      \\  \\
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ~~~~        ~~~~~~    ~~~~~~~~~
    ~~~~~~~  ~~~~~~  ~~~~~~
      ~~~~~~~~  ~~~~~~~~~~~~
'''

    print(scene)

def cave_scene():
    scene = '''
      /\\      /\\
     /  \\    /  \\     /\\
    /    \\  /    \\   /  \\
   /      \\/      \\ /    \\
  /   __           /      \\
 /   /  \\_________ \\  /\\  \\
/___/        _____  \\/  \\  \\
|      _____/     \\  \\    \\|
|_____/     \\      \\_|     |
|     |      \\      |      |
|     |       \\     |      |
|_____|        \\____|______|
    '''
    print(scene)
    
#define reusable game header
def game_header():
    #clear terminal
    print("\n" * 100)
    #game header
    print(f"#######################")
    print(f"# Wilderness Survival #")
    print(f"#######################\n")



#setup game and player name


    



#main_character.add_item(magic_mushroom, 5)
#magic_mushroom.use(main_character)
#bear.attack(main_character)
#
