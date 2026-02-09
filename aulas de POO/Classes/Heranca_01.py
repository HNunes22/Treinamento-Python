class Animal:
    def __init__(self, animal_name, animal_color, animal_specie):
        self.name = animal_name
        self.color = animal_color
        self.specie = animal_specie

    def geeting(self):
        print(f"Hello, My name is {self.name}, I'm  {self.specie}")

class Dog(Animal):
    def growl(self):
        print("Growing Dog")

dog01 = Dog("Bob", "Light Gray", "Snowy")
dog01.geeting()
dog01.growl()