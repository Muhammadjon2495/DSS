class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


car = Vehicle(180, 12)

print("Max Speed:", car.max_speed)
print("Mileage:", car.mileage)