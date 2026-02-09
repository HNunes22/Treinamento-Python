class Person:
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

class Employee(Person):
    def __init__(self, person_name, person_age, position):
        super().__init__(person_name, person_age)
        self.position = position

    def show_characteristics(self):
        print(f"Name: {self.name}\n"
              f"Position: {self.position}")

class Client(Person):
    def __init__(self, person_name, person_age):
        super().__init__(person_name, person_age)
        self.wallet = 0

    def show_myWallet(self):
        print(f"Hi Mr.(s) {self.name} your wallet is ${self.wallet}")

    def deposit_in_myWallet(self, ammout):
        if ammout > 0:
            self.wallet += ammout
            print("Success Deposit")
        else:
            print("Failed Deposit. Please, try again.")


employee1 = Employee("Alpha", 33, "Dev Junior")
employee1.show_characteristics()

client1 = Client("Mario", 67)
client1.deposit_in_myWallet(0)
client1.show_myWallet()