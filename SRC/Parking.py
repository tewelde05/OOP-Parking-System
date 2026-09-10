# class ParkingLot:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.parked_cars = []

#     def park_car(self, car):
#         if len(self.parked_cars) < self.capacity:
#             self.parked_cars.append(car)
#             print(f"{car.license_plate} parked successfully.")
#         else:
#             print("Parking lot is full.")

#     def remove_car(self, license_plate):
#         for car in self.parked_cars:
#             if car.license_plate == license_plate:
#                 self.parked_cars.remove(car)
#                 print(f"{license_plate} left the parking lot.")
#                 return

#         print("Car not found.")

#     def show_cars(self):
#         if not self.parked_cars:
#             print("No cars are currently parked.")
#         else:
#             print("\nCars currently parked:")

#             for car in self.parked_cars:
#                 print(car.display_info())
class Parking:
    def __init__(self, parking_number):
        self.parking_number = parking_number
        self.car = None

    def park_car(self, car):
        self.car = car
        print(f"{car.name} is allocated Parking {self.parking_number}")
