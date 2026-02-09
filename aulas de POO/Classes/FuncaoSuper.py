# School System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.stats = "Inactive"
    def greeting(self):
        print(f"Name: {self.name}\nAge: {self.age}\nStatus: {self.stats}\n")

    def activate_status(self, stats):
        if stats != True and stats != False:
            print("Status must be True(Active) or False(Inactive)")
            self.stats = "Inactive"
        elif stats == self.stats:
            print(f"Status is {self.stats}")
        else:
            self.stats = "Active"
            print("Change Status!")

class Student(Person):
    def __init__(self, name, age, year_school):
        super().__init__(name, age)
        self.score = year_school

    def greeting(self):
        super().greeting()
        print(f"Hi!, My name is {self.name} and I am {self.age} years old.\n")

class Teacher(Person):
    def __init__(self, name, age, discipline):
        super().__init__(name, age)
        self.score = discipline

class Assistant(Person):
    def __init__(self, name, age, block):
        super().__init__(name, age)
        self.score = block

st1 = Student("Alpha", 13, 7)
#st1.Greeting()
st1.activate_status(True)
st1.greeting()

te1 = Teacher("Beta", 55, "Biology")
te1.greeting()

as1 = Assistant("Charlie", 23, "Block Biology")
as1.greeting()

