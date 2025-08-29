# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, contact):
        print(f"Calling {contact} from {self.brand} {self.model}...")
    
    def info(self):
        print(f"{self.brand} {self.model} with {self.storage}GB storage")

# Child Class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)  # inherit attributes from Smartphone
        self.cooling_system = cooling_system
    
    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system 🚀")

# Create objects
phone1 = Smartphone("Samsung", "S24", 256)
phone1.info()
phone1.call("Alice")

phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "liquid cooling")
phone2.info()
phone2.play_game("Genshin Impact")

# Base Class
class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

# Child Classes with Polymorphism
class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Show polymorphism in action
for v in vehicles:
    v.move()
