from functions import *
from player import *

class Threat:
    def __init__(self):
        self.name = ''
        self.description = ''

    def get_description(self):
        return self.description
    
class Bear(Threat):
    """create bear class"""
    def __init__(self):
        super().__init__()
        self.name = 'Bear'
        self.description = "A massive bear with matted fur and glinting eyes, a powerful force of nature."
        self.health = 50
        self.damage = 20

    def attack(self, target):
        self.target = target
        print_fast(f"The massive beast lunges at you!")
        attack_die = dice(20)
        if attack_die > 8:
            target.take_damage(self.damage)
            

        elif attack_die == 20:
            print_fast(f"CRITICAL HIT")
            critical_hit = self.damage * 1.5
            target.take_damage(critical_hit)
            

        else:
            print_fast(f"The bear swings wildly and misses wildly.")