from swap_meet.item import Item

class Vendor:

######################################## WAVE 1 #########################################
    
    def __init__(self, inventory=None, modifier=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        self.modifier = modifier


    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except:
            return False


######################################## WAVE 2 #########################################

    def get_by_category(self, category):
        category_items = [item for item in self.inventory if item.category == category]
        return category_items


######################################## WAVE 3 #########################################

    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory and their_item in other.inventory:
            self.add(other.remove(their_item))
            other.add(self.remove(my_item))
            return True
        else: 
            return False


######################################## WAVE 4 #########################################

    def swap_first_item(self, other):
        try:
            return self.swap_items(other, self.inventory[0],other.inventory[0])
        except:
            return False


######################################## WAVE 6 #########################################

    def get_best_by_category(self, category):
        try:
            best_item = max(self.get_by_category(category), key=lambda item:item.condition)
            return best_item
        except:
            return None


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_offer =  self.get_best_by_category(their_priority)
        their_offer = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_offer, their_offer)


######################################## WAVE 7 #########################################

    def get_newest(self):
        try:
            newest_item = min(self.inventory, key=lambda item:item.age)
            return newest_item
        except:
            return None

    def swap_by_newest(self, other):
        my_offer =  self.get_newest()
        their_offer = other.get_newest()
        return self.swap_items(other, my_offer, their_offer)

