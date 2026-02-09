# Polymorphism

class Class:
    def __init__(self):
        self.power = 0
        self.defense = 0
        self.speed = 0
        self.lucky = 0

    def stats_print(self):
        print(f"Power: {self.power}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print(f"Lucky: {self.lucky}")
        print()

class Assassin(Class):
    def initialization(self):
        self.power = 8
        self.defense = 2
        self.speed = 9
        self.lucky = 4
        return "Create Assassin"

class Archer(Class):
    def initialization(self):
        self.power = 5
        self.defense = 1
        self.speed = 7
        self.lucky = 7
        return "Create Archer"

class Mage(Class):
    def initialization(self):
        self.power = 10
        self.defense = 1
        self.speed = 5
        self.lucky = 8
        return "Create Mage"

# Create the Objects

persons = [Assassin(), Archer(), Mage()]

for person in persons:
    person.initialization()
    person.stats_print()

'''
assassin1 = Assassin()
assassin1.initialization()
assassin1.stats_print()

archer1 = Archer()
archer1.initialization()
archer1.stats_print()

mage1 = Mage()
mage1.initialization()
mage1.stats_print()
'''