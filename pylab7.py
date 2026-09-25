class Vehicle7:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus7(Vehicle7):
    pass


school_bus7 = Bus7("School Volvo", 12, 50)

print("\nlab 7")

if isinstance(school_bus7, Bus7):
    print("School_bus is a Bus object")
else:
    print("School_bus is not a Bus object")
