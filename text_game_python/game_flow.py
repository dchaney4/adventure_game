from game_functions import *


########more color. green for items?

def game_setup():
    game_header()
    river_scene()
    print_slow(f"Enter your name to play or quit to exit game.")
    #run name_player function to ask for input and save player.name
    main_character.name_player()

    #quit exits game
    if main_character.name.lower() == 'quit':
        quit_game()
    #invalid name check - restarts prompt 
    elif main_character.name.isspace() == 1 or main_character.name == '':
        print(f"Invalid name, please try again..")
        time.sleep(2)
        game_setup()
    #run game_start with name saved
    else:
        print_fast(f"Sweep all of the bugs under the furniture and roll out the red carpet!\nThe Java Juggler, Code Conjurer, Syntax Sorcerer {main_character.name} has arrived!")
        time.sleep(6)
        game_start()



#print header and game intro
def game_start():
    game_header()
    print_slow(f"The trip of a lifetime...")
    print_slow(f"Adventure is calling..")
    print_slow(f'''"You're crazy!".."You won't make it out alive".."Please, be careful"..''')
    print_slow(".   .   .  ")
    time.sleep(2)
    print_slow("")
    #print_slow(f'''\x1B[3m~Three nights since you had set out on a solo adventure into the forest.. Lost and anxious, you look at your map again..~''')
    #print_slow(f'''~"Dammit!" Maybe I shouldn't have ventured off-trail~\x1B[0m''')
    #print_slow(".   .   .  ")
    #time.sleep(2)
    print_slow(f"You finally emerge from the woods and stumble onto a narrow deer trail.")
    print_slow(f"This trail is flanked by dense brush on both sides and runs north to south.")
    print_slow(f"Which way will you go? Type help for basic commands.")
    trail_choice()

    #choose north or south on trail
def trail_choice():
    choice = get_input(['north', 'south', 's', 'n'], "It's not that complicated.. north or south?")
    
    if choice == 'south' or choice == 's':
        trail_south()
    elif choice == 'north' or choice == 'n':
        trail_north()
    else:
        print(error_message)
        trail_choice()

#heading south down the trail - bear encounter
first_trail_south = True

def trail_south():
    global first_trail_south
    move_player(south_trail)
    game_header()
    
    if first_trail_south:
        print_slow(f"Traveling south down the trail for several minutes as the sun begins to set to your right.")
        print_slow(f"\x1B[3m~I'll need to set up camp soon..~\x1B[0m")
        print_slow(f"Do you continue south?")
        first_trail_south = False
    else:
        print_slow("This familiar trail runs north to south. There is a musty odor in the air.")
        print_slow("Which way?")

    choice = get_input(['north', 'south', 'continue', 'yes', 'y', 'no'], "It's not that complicated.. north or south?")
    if choice in ['south', 'continue', 'yes', 'y']:
        bear_cave_story()
    elif choice in ['north', 'no']:
        trail_north()
    else:
        print(error_message)
        trail_south()

first_trail_north = True
def trail_north():
    global first_trail_north
    move_player(north_trail)
    game_header()

    if first_trail_north:
        print_slow(f"Traveling north down the trail for several minutes as the sun begins to set to your left.")
        print_slow(f"\x1B[3m~I'll need to set up camp soon..~\x1B[0m")
        print_slow("Do you continue north?")
        first_trail_north = False
    else:
        print_slow("This familiar trail runs north to south with large fallen branches scattered.")
        print_slow("Which way?")


    choice = get_input(['north', 'south', 'continue', 'yes', 'y', 'no'], "It's not that complicated.. north or south?")
    if choice in ['south', 'n', 'no']:
        trail_south()
    elif choice in ['north', 'yes', 'y']:
        river_bed()
    else:
        print(error_message)
        trail_north()

def bear_cave_story():
    move_player(bear_cave)
    game_header()
    cave_scene()
    print_slow(f"The trail opens up to reveal a cave entrance, shrouded in ferns and moss.")
    if bear_cave.nearby_threats == None:
        print("Do you enter the cave?")
        bear_choice()
    else:
        print_slow(f"You see a large, dark shape crouched near the entrance..")
        print_fast(f"Oh shit, it's a bear! What are you going to do?!")
        bear_choice()

def bear_choice():
    initial_choices = ['run', 'fight', 'attack', 'die', 'enter', 'enter cave', 'leave', 'north', 'n', 'trail']

    if bear_cave.nearby_threats is None:
        valid_choices = [choice for choice in initial_choices if choice not in ['fight', 'attack', 'run', 'die']]
    else:
        valid_choices = [choice for choice in initial_choices if choice not in ['enter', 'enter cave', 'leave', 'n', 'north', 'trail']]

    if bear.health > 0:
        choice = get_input(valid_choices, "Hint: don't poke the bear")
        
        
        if choice == 'fight' or choice == 'attack':
            print_fast(f"Okay {main_character.name}, you must be a masochist then. Good luck fighting the fucking bear..")
            
            if main_character.equipped_weapon == None:
                main_character.attack(bear)
                bear.attack(main_character)
                bear_choice()

            if main_character.equipped_weapon.name == 'Bear Spray':
                main_character.attack(bear)
                if bear.health <= 80:
                    print_fast("The bear writhes in pain and runs off into the forest.")
                    print_fast("You could enter the cave now.. If you dare.")
                    bear_cave.remove_threat(bear)
                    bear_choice()
                else:
                    bear.attack(main_character)
                    bear_choice()
            else:
                main_character.attack(bear)
                bear.attack(main_character)
                bear_choice()

        elif choice == 'die':
            print_slow(f"No honor in suicide by bear..")
            while(True):
                bear.attack(main_character)
        
        elif choice == 'run':
            escape = dice(20)
            if escape > 5:
                print_slow(f"You successfully flee the bear.. atleast for now.")
                trail_south()
            else:
                print_fast("The bear chases you down and attacks!")
                bear.attack(main_character)
                bear_choice()

    else:

        choice = get_input(valid_choices, "You could enter the cave or return to the trail")
        if choice == 'enter' or choice == 'enter cave':
            print_slow("You nervously slink into the dark cave..")
            bear_cave_interior()

        elif choice in ['leave', 'north', 'n', 'trail']:
            print_slow("You head back the way you came.")
            trail_south()

        else:
            print_slow(choice.error_message)
            bear_choice()

def bear_cave_interior():
    move_player(bear_cave_interior_area)
    print_slow("The temperature drops 10 degrees as you enter the damp cave.\nAs your eyes adjust, you see that the cave is not that deep and seemingly empty.\nYou decide to make camp for the night.\nCongrats, you won I guess.")
    time.sleep(5)
    quit_game()

def river_bed():
    move_player(river_area)
    print_slow("A beautiful sunset illuminates a river bed that runs east to west. You can see that the river travels along for quite awhile in both directions.\nThe north-south trail you were on also continues across the river.")
    choice = get_input(['east', 'west', 'north', 'south', 'n', 's', 'w', 'e'], "Which direction do you go?")
    if choice == 'east' or choice == 'e':
        east_river()
    if choice == 'west' or choice == 'w':
        west_river()
    if choice == 'north' or choice == 'n':
        far_trail_north()
    if choice == 'south' or choice == 's':
        trail_north()

def east_river():
    print_slow("under construction..")
    river_bed()

def west_river():
    print_slow("under construction..")
    river_bed()

def far_trail_north():
    print_slow("under construction..")
    river_bed()

#start game - move to play_game?
if __name__ == "__main__":
    game_setup()
