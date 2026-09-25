class Vehicle5:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus5(Vehicle5):
    pass


class Car5(Vehicle5):
    pass


school_bus5 = Bus5("School Volvo", 180, 12)
car5 = Car5("Audi Q5", 240, 18)

print("\nlab 5")
print(
    "Color:",
    school_bus5.color,
    "Vehicle name:",
    school_bus5.name,
    "Speed:",
    school_bus5.max_speed,
    "Mileage:",
    school_bus5.mileage
)

print(
    "Color:",
    car5.color,
    "Vehicle name:",
    car5.name,
    "Speed:",
    car5.max_speed,
    "Mileage:",
    car5.mileage
)
