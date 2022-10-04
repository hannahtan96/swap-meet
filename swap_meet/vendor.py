from re import T
from tkinter.tix import Tree
from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = []


    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except:
            return False


    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]


    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            self.add(other.remove(their_item))
            other.add(self.remove(my_item))
            return True
        else: 
            return False


    def swap_first_item(self, other):
        try:
            return self.swap_items(other, self.inventory[0],other.inventory[0])
        except:
            return False


    def get_best_by_category(self, category):
        best_item = None
        highest_condition = -1
        for item in self.inventory:
            if item.condition > highest_condition and item.category == category:
                best_item = item
                highest_condition = item.condition
        return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_offer =  self.get_best_by_category(their_priority)
        their_offer = other.get_best_by_category(my_priority)
        if my_offer and their_offer:
            self.swap_items(other, my_offer, their_offer)
            return True
        else:
            return False


    def get_newest(self):
        try:
            newest_item = self.inventory[0]
        except:
            return None
        
        lowest_age = newest_item.age
        for item in self.inventory:
            if item.age < lowest_age:
                newest_item = item
                lowest_age = item.age
        return newest_item


    def swap_by_newest(self, other):
        my_offer =  self.get_newest()
        their_offer = other.get_newest()
        if my_offer and their_offer:
            self.swap_items(other, my_offer, their_offer)
            return True
        else:
            return False

