class Vehicle4:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus4(Vehicle4):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


bus4 = Bus4("bus", 180, 12)

print("\nExercise 4")
print(bus4.seating_capacity())

