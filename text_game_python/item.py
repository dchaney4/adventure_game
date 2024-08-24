from functions import *
import random


#heal = add health
#damage = lose health
#recover = add hunger
#hunger = lose hunger



class Item:
    """Generic item class creation"""
    def __init__(self, quantity = 0):
        self.name = ''
        self.description = ''
        self.quantity = quantity
        self.type = ''

    
class Club(Item):
    def __init__(self, quantity = 0):
        super().__init__()
        self.damage = 20
        self.type = 'Weapon'
        self.name = 'Club'
        self.quantity = quantity
        self.description = (f"It's just a large stick. Good for hitting things. Deals {self.damage} points of damage.")
        self.aliases = ['branch', 'stick']

    def use(self, player):
        print_slow(f"Try attacking when the time is right..")

class BearSpray(Item):
    def __init__(self, quantity = 0):
        super().__init__()
        self.damage = 20
        self.type = 'Weapon'
        self.name = 'Bear Spray'
        self.quantity = quantity
        self.description = (f"A dented can of bear spray. The logo reads, \"For When 'Shoo Bear' Just Won't Do!\"  Deals {self.damage} points of damage.")
        self.aliases = ['spray', 'mace']
        
    def use(self, player):
        print_slow(f"Try attacking when the time is right..")


class Bandage(Item):
    """bandage that heals 10 hp"""
    def __init__(self, quantity = 0):
        super().__init__()
        #healing set to 10
        self.name = 'Bandage'
        self.healing_amount = 10
        self.quantity = quantity
        self.type = 'Consumable'
        self.description = (f"Clean bandages that heal {self.healing_amount} health.")
        self.aliases = ['bandages']
    
    def use(self, player):
        #check to see if item is in inventory
        if self.quantity <= 0:
            print_slow(f"No {self.name} available")
            return
        else:
            print_slow(f"{self.name} used.")

        #heal up to healing amount and up to max health
        player.heal(self.healing_amount)

        #remove used bandage
        self.quantity -= 1
        if self.quantity < 1:
            player.remove_item(self)


class Magic_Mushroom(Item):
    """magic mushroom item, damages health and heals hunger"""
    def __init__(self, quantity = 0):
        super().__init__()
        self.name = 'Magic Mushroom'
        self.quantity = quantity
        self.description = 'Amanita Muscaria- consume with caution'
        self.recover_amount = 20
        self.damage_amount = 10
        self.type = 'Consumable'
        self.aliases = ['mushroom', 'fungi', 'shroom', 'fungus']
    
    def use(self, player):
        #check inventory for item
        if self.quantity <= 0:
            print_fast(f"No {self.name} available")
            return
        else:
            print_fast(f"{self.name} eaten.")

        #random event- nat 20, you regain max health and hunger; nat 1, instant death
        d20 = dice(20)
        if d20 == 1:
            print_slow(f"Dying alone wasn't enough. Instead you chose to go out the easy way, high on mushrooms..")
            player.take_damage(player.health)
        elif d20 == 20:
            print_fast(f"\033[1;31;40mSuper Mushroom Power-up! You now have max health and hunger.\033[0m")
            player.hunger = player.max_hunger
            player.health = player.max_health

        #if not a 1 or 20, execute typical effect
        else:

            player.take_damage(self.damage_amount)

            player.recover_hunger(self.recover_amount)

            #remove from inventory
        self.quantity -= 1
        if self.quantity < 1:
            player.remove_item(self)

class TrailMix(Item):
    """Trail Mix that recover 10 hunger"""
    def __init__(self, quantity = 0):
        super().__init__()
        self.name = 'Trail Mix'
        self.quantity = quantity
        self.recover_amount = 10
        self.type = 'Consumable'
        self.description = (f"A classic mix of nuts, seeds, and dried fruits. Recovers {self.recover_amount} hunger")

    def use(self, player):
        #check to see if item is in inventory
        if self.quantity <= 0:
            print_slow(f"No {self.name} available")
            return
        else:
            print_slow(f"{self.name} used.")

        #recover hunger
        player.recover_hunger(self.recover_amount)

        #remove used trail mix
        self.quantity -= 1
        if self.quantity < 1:
            player.remove_item(self)


            
 





#implement methods for adding and reducing health and hunger in player class. with message prompting for status updates (ie. stomach growling)