class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def describe_car(self):
        print(f"The car is {self.make} {self.model} manufactured in {self.year}")

myobj=Car("Ford","Everest",2018)
myobj.describe_car()
myobj_2 = Car("Nissan","Miata",2001)
myobj_2.describe_car()