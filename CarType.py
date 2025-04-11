class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Collect user input
print("Let's enter details for your car:")
year = input("Year: ")
make = input("Make: ")
model = input("Model: ")
doors = input("Number of doors (2 or 4): ")
roof = input("Type of roof (solid or sun roof): ")

# Create an Automobile object
car = Automobile("car", year, make, model, doors, roof)

# Display car details
print("\nVehicle Information:")
print(f"  Vehicle type: {car.vehicleType}")
print(f"  Year: {car.year}")
print(f"  Make: {car.make}")
print(f"  Model: {car.model}")
print(f"  Number of doors: {car.doors}")
print(f"  Type of roof: {car.roof}")