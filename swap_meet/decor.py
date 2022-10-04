from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, condition=0, age=0):
        super().__init__(self, condition, age)
        self.category = "Decor"

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        return super().condition_description()