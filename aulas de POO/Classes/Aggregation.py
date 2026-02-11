# Aggregation

class Engine:
    def __init__(self, logo, power):
        self.logo = logo
        self.power = power


class Car:
    def __init__(self):
        self.engines = []

    def add_new_engine(self, engine):
        self.engines.append(engine)

    def show_engines(self):
        for engine in self.engines:
            print(f"Marca: {engine.logo} - Power: {engine.power}")


# Create the news engines

engine_v6 = Engine("Ford", 300)
engine_v8 = Engine("Mustang", 600)

# Create a car and add engine
car = Car()
car.add_new_engine(engine_v6)
car.add_new_engine(engine_v8)

# List

car.show_engines()