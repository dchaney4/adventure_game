from functions import *
from item import *
from player import *
from threat import *


class Area:
    def __init__(self, description, alt_description, nearby_items = None, nearby_threats = None, trigger_condition = None):
        self.original_description = description
        self.alt_description = alt_description
        self.current_description = description
        self.nearby_items = nearby_items or []
        self.nearby_threats = nearby_threats or []
        self.trigger_condition = trigger_condition

    def check_condition(self):
        if self.trigger_condition and self.trigger_condition(self):
            self.current_description = self.alt_description

    def remove_items(self, item):
        for i, (area_item, quantity) in enumerate(self.nearby_items):
            if area_item.name == item.name:
                del self.nearby_items[i]
                break
        self.check_condition()

    def remove_threat(self, threat):
        if threat in self.nearby_threats:
            self.nearby_threats.remove(threat)
        
        self.check_condition()


    def get_description(self):
        base_description = self.current_description
        return base_description




