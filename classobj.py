class Gari:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odo_reading = 0
    def describe_car(self):
        print(f"The {self.make} {self.model} {self.year} has {self.odo_reading} miles on it")
    def read_odo(self):
        print(f"{self.odo_reading}")
    def update_odo(self, milage):
        if milage >= self.odo_reading:
            self.odo_reading = milage
        else:
            print("You can't")
    def increment_odo(self,miles):
        self.odo_reading +=miles

my_gari = Gari("Toyota","Yaris","2022")
print(my_gari.describe_car())
print(my_gari.read_odo())
my_gari.update_odo(100)
my_gari.increment_odo(50)
my_gari.describe_car()