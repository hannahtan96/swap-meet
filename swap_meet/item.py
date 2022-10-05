CONDITION_DESC = {
    0: "you might as well buy a new one",
    1: "barely hanging on",
    2: "pretty used",
    3: "kinda used",
    4: "newish",
    5: "mint"
}

class Item:
    
    def __init__(self, category='', condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

######################################## WAVE 5 #########################################

    def condition_description(self):
        return CONDITION_DESC[int(self.condition)]
