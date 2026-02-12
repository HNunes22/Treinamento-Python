def sum_numbers(*numbers): # Create a tuple of numbers
    return sum(numbers)

result = sum_numbers(1,4,5,6,7,8,11)

print(result)

def create_car(**car):
    return car

car1 = create_car(model="Gol", year=2000, color="White Gray")

print(car1)