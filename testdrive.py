from app import Car, Truck, Boat


# Test driver code
if __name__ == "__main__":
    # Create instances of Vehicle Car
    car = Car("Toyota", "Corolla", 2021, 1275.0, 4)
    truck = Truck("Mac", "Street 750", 2019, 220.0, 2, 5000) #<--- but this now takes truck's constructor.
    boat = Boat("Sea Doo", "RXT-X", 2020, 1000, "Jet Ski")

    # Display information of the car
    print("Car Info:")
    car.display_info()
    car.honk()
    print()


    # Display information of the mac truck
    print("Truck Info:")
    truck.display_info()
    truck.honk()
    print()


    #display information of the Sea Doo
    print("Boat Info:")
    boat.display_info()
    boat.honk()
    print()



