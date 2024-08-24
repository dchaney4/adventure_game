from item import *
from functions import *


#generic player class, only used for main character currently
class Player:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.max_health = 100
        self.hunger = 100
        self.max_hunger = 100
        self.inventory = []
        self.equipped_weapon = None
        self.current_area = None

    def name_player(self):
        self.name = input('>')
        
    def player_status(self):
        status = f"Name: \033[1;32;40m{self.name}\033[0m Health:\033[1;31;40m{self.health}/{self.max_health}\033[0m Hunger: \033[1;33;40m{self.hunger}/{self.max_hunger}\033[0m"
        return status
        
    ##INVENTORY MANAGEMENT##
    def use_item(self, item_name):
        #checking for vowels
        vowels = 'aeiou'
        article = 'an' if item_name[0].lower() in vowels else 'a'

        #check if item is in inventory// runs item.use function
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                return

        print_slow(f"You do not have {article} {item_name} in your inventory.")

    # add item to inventory
    def add_item(self, item, quantity):
        for inv_item in self.inventory: #if item is already in inventory, add to item.quantity
            if inv_item.name.lower() == item.name.lower():
                item.quantity += quantity
                if quantity > 1:
                    print_slow(f"{quantity} {item.name}s added to inventory.")
                else:
                    print_slow(f"{quantity} {item.name} added to inventory.")
                return

        #if not in inventory create new instance
        new_item = item.__class__()
        new_item.quantity = quantity
        self.inventory.append(item)
        item.quantity = quantity
        if quantity > 1:
            print_slow(f"{quantity} {item.name}s added to inventory.")
        else:
            print_slow(f"{quantity} {item.name} added to inventory.")
        
        
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def inspect_item(self, item_name):

        #checking for vowels
        vowels = 'aeiou'
        article = 'an' if item_name[0].lower() in vowels else 'a'

        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                print_slow(item.description)
                return

        print_slow(f"You do not have {article} {item_name} in your inventory.")

    def equip_weapon(self, item_name):

        #checking for vowels
        vowels = 'aeiou'
        article = 'an' if item_name[0].lower() in vowels else 'a'
        weapon_found = False

        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item.type == 'Weapon': 
                    self.equipped_weapon = item
                    print_slow(f"You have equipped {article} {item.name}.")
                    weapon_found = True
                    break
                else:
                    print_slow(f"{item.name} is not a weapon.")
                    weapon_found = True
                    break

        if not weapon_found:
            print_slow(f"You do not have {article} {item_name} in your inventory.")

    #pick up item from area.nearby_items
    def pickup_item(self, item_name):
        if self.current_area is None:
            print("Nothing to pick up..")
            return
        
        for item, quantity in self.current_area.nearby_items:
            if item_name.lower() == item.name.lower() or item_name.lower() in [alias.lower() for alias in item.aliases]:
                self.add_item(item, quantity)
                self.current_area.remove_items(item)
                return
                
        print_slow(f"{item_name} not found.")
            
    ##HEALTH AND HUNGER MUTATORS##
    def heal(self, amount):
        heal_count = 0
        while self.health < self.max_health and heal_count < amount:
            heal_count += 1
            self.health += 1
        if heal_count == 0:
            print(f"\033[0;32m{self.name} is already at max health!\033[0m")

        elif heal_count == 1:
            if self.health == self.max_health:
                print(f"\033[0;32m{self.name} healed for {heal_count} point and is now at max health.\033[0m")
            else:
                print(f"\033[0;32m{self.name} healed for {heal_count} point.\033[0m")
        
        else:
            if self.health == self.max_health:
                print(f"\033[0;32m{self.name} healed for {heal_count} points and is now at max health.\033[0m")
            else:
                print(f"\033[0;32m{self.name} healed for {heal_count} points.\033[0m") 
        
    def take_damage(self, damage):
        self.health = self.health - damage
        if damage == 1:
            print_fast(f"\033[0;31m{self.name} took {damage} point of damage.\033[0m")
        else:
            print_fast(f"\033[0;31m{self.name} took {damage} points of damage.\033[0m")

        if self.health < 75 and self.health >= 50:
            print_fast(f"\033[1;33m'Tis but a scratch\033[0m")
        elif self.health < 50 and self.health >= 25:
            print_fast(f"\033[0;31mUhh, you are supposed to stay alive remember\033[0m")
        elif self.health < 25 and self.health > 0:
            print_fast(f"\033[1;31mYou are going to die out here and no one will find your body..\033[0m")
        elif self.health <= 0:
            print_slow(f"\033[1;31m{self.name} is dead.\033[0m\nBetter luck next time.")
            exit()

    def reduce_hunger(self, amount):
        hunger_count = 0
        while self.hunger > 0 and hunger_count < amount:
            hunger_count += 1
            self.hunger -= 1
        
        if self.hunger < 75 and self.hunger >= 50:
            print_slow(f"\033[1;33mYour stomach begins to rumble.\033[0m")
        elif self.hunger < 50 and self.hunger >= 25:
            print_slow(f"\033[1;33mThat would be embarrasing to die of hunger..\033[0m")
        elif self.hunger < 25:
            print_slow(f"\033[1;31mYou are starving! Should've packed more granola.\033[0m")

    def recover_hunger(self, amount):
        recover_count=0
        while self.hunger < self.max_hunger and recover_count < amount:
            recover_count += 1
            self.hunger += 1
 
        if self.hunger == self.max_hunger:
            print_slow(f"\033[0;32m{self.name} recovered {recover_count} hunger and is now full.\033[0m")
        else:
            print_slow(f"\033[0;32m{self.name} has recovered {recover_count} hunger.\033[0m")

    
    #clock ticks and health and hunger decrease
    def ticking_clock(self):
        print(f"\033[0;31mThe clock is ticking..\033[0m")
        number = dice(10)
        self.reduce_hunger(number)

        if self.hunger < 25:
            number = dice(8)
            self.take_damage(number)
        elif self.hunger == 0:
            number = dice(12)
            self.take_damage(number)
        else:
            number = dice(4)
            self.take_damage(number)

        time.sleep(2.5)
            
    def attack(self, target):
        hit_chance = dice(20)
        #path for uneqquiped
        if self.equipped_weapon == None:
            print_fast(f"You attack with your fists.")
            fist_damage = dice(4)
            #crit damage
            if hit_chance == 20:
                crit_damage = fist_damage * 1.5
                target.health -= crit_damage
                print_fast("CRITICAL HIT")
                if target.health <= 0:
                    print_fast(f"\033[0;32mDealing {crit_damage} points of damage and the {target.name} is dead!\033[0m")
                else:
                    print_fast(f"\033[0;32mDealing {crit_damage} points of damage to the {target.name}!\033[0m")
            #Normal attack
            elif hit_chance < 20 and hit_chance > 5:
                damage = fist_damage
                target.health -= damage
                if target.health <= 0:
                    print_fast(f"\033[0;32mDealing {damage} points of damage and the {target.name} is dead!\033[0m")
                else:
                    print_fast(f"\033[0;32mDealing {damage} points of damage to the {target.name}!\033[0m")
            else:
                print_fast(f"Your attack misses the {target.name}")

        #path with equipped weapon
        else:

            print_fast(f"You attack with your {self.equipped_weapon.name}.")        
            if hit_chance == 20:
                crit_damage = self.equipped_weapon.damage * 1.5
                target.health -= crit_damage
                print_fast("CRITICAL HIT")
                if target.health <= 0:
                    print_fast(f"\033[0;32mYou dealt {crit_damage} points of damage and the {target.name} is dead!\033[0m")
                else:
                    print_fast(f"\033[0;32mYou dealt {crit_damage} points of damage to the {target.name}!\033[0m")
            elif hit_chance < 20 and hit_chance > 5:
                damage = self.equipped_weapon.damage
                target.health -= damage
                if target.health <= 0:
                    print_fast(f"\033[0;32mYou dealt {damage} points of damage and the {target.name} is dead!\033[0m")
                else:
                    print_fast(f"\033[0;32mYou dealt {damage} points of damage to the {target.name}!\033[0m")
            else:
                print_fast(f"Your attack missed the {target.name}.\033[0m")

  