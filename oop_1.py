class Fruits:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def display_fruits(self):
        print(f"A/An {self.name} is Ksh {self.price}")

fruit1 = Fruits("Apple",35)
fruit2 = Fruits("Banana",5)
fruit3 = Fruits("Cherry",10)
fruit4 = Fruits("Orange",10)
fruit5 = Fruits("Pear",20)
fruit6 = Fruits("Mango",20)


fruit1.display_fruits()
fruit2.display_fruits()
fruit3.display_fruits()
fruit4.display_fruits()
fruit5.display_fruits()
fruit6.display_fruits()