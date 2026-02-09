# Multiple Herance and Multilevel

    # Class Grandfather

class Animal:
    def __init__(self, name):
        self.name = name
        
    # Class Father

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} Hunting the Prey...")


class Prey(Animal):
    def runing(self):
        print(f"{self.name} Running from the Hunter...")

    # Class Children

class Rabbit(Prey):
    pass

class Fox(Predator):
    pass

class Dolphin(Predator, Prey):
    pass


rabbit1 = Rabbit("David")

rabbit1.runing()

fox1 = Fox("Delphox")

fox1.hunt()

