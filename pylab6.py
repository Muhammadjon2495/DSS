class Vehicle6:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus6(Vehicle6):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 0.10
        return total_fare + maintenance_charge


school_bus6 = Bus6("School Volvo", 12, 50)

print("\nExercise 6")
print("Total Bus fare is:", school_bus6.fare())

