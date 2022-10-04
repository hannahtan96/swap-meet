class Item:
    
    def __init__(self, category='', condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "mint"
        elif self.condition == 4:
            return "newish"
        elif self.condition == 3:
            return "kinda used"
        elif self.condition == 2:
            return "pretty used"
        elif self.condition == 1:
            return "barely hanging on"
        elif self.condition == 0:
            return "you might as well buy a new one"
