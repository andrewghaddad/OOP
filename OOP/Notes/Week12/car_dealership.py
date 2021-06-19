# Buyer
# Car
# A Car has Buyer

# name, address, phone
# when we print a Buyer
#   'name' lives in 'address' and can be contacted at 'phone'
class Buyer():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return self.name + " lives in " + self.address + " and can be contacted at " + self.phone

# make, color, buyer
# there should be a way to set the buyer of a car
# when we print a car
#   This car is a 'color' 'make' that belongs to 'buyer'
class Car():
    def __init__(self, make, color, buyer):
        self.make = make
        self.color = color
        self.buyer = buyer

    def __str__(self):
        return "This car is a " + self.color + " " + self.make + " that belongs to " + self.buyer.name

    def set_buyer(self, buyer):
        self.buyer = buyer

bob = Buyer("Bob", "1000 Main St.", "9876543210")
print(bob)
alice = Buyer("Alice", "2000 Somewhere St.", "1234567890")
print(alice)

bob_car = Car("Lamborghini", "black", bob)
print(bob_car)
alice_car = Car("Bugatti", "red", alice)
print(alice_car)

bob_car = alice_car
bob_car.set_buyer(bob)
print(alice_car)
print(bob_car)
alice_car = None
print(alice_car)
print(bob_car)