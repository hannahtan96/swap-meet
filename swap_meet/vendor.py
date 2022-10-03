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

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(other_vendor.remove(their_item))
            other_vendor.add(self.remove(my_item))
            return True
        else: 
            return False
