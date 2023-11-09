
class Car:
    #constructor
    def __init__(self, make, model, year, weight, num_doors):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors

    #prints attributes of a car
    def display_info(self):
        print(f'Make: {self.make} Model: {self.model} Year: {self.year} Weight: {self.weight} Num. Doors: {self.num_doors}')

    def honk(self):
        print("HONK")



#boats have a type instead of a number of doors
class Boat:
    def __init__(self, make, model, year, weight, type):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.type = type

    def display_info(self):
        print(f'Make: {self.make} Model: {self.model} Year: {self.year} Weight: {self.weight} Boat Type: {self.type}')

    def honk(self):
        print("BOOOOO-OOOO")


#trucks have everything cars have but also have a payload capacity
class Truck:
    def __init__(self, make, model, year, weight, num_doors, payload_capacity):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors
        self.payload_capacity = payload_capacity

    def display_info(self):
        print(f'Make: {self.make} Model: {self.model} Year: {self.year} Weight: {self.weight} Num. Doors: {self.num_doors} Payload Capacity: {self.payload_capacity}')

    def honk(self):
        print("BUUUUAAAAAAAA")

    def dump_load(self):
        print("DUMPING LOAD... BOOM")




