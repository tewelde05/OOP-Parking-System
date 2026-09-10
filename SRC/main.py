# from Car import Car
# from Parking import ParkingLot


# def main():
#     parking = ParkingLot(3)

#     car1 = Car("ABC123", "Senay")
#     car2 = Car("XYZ456", "John")
#     car3 = Car("DEF789", "Sara")

#     parking.park_car(car1)
#     parking.park_car(car2)
#     parking.park_car(car3)

#     parking.show_cars()

#     parking.remove_car("XYZ456")

#     parking.show_cars()


# if __name__ == "__main__":
#     main()
from Car import Car
from Parking import Parking


def main():
    car_a = Car("Car A")
    car_b = Car("Car B")

    parking_001 = Parking("001")
    parking_002 = Parking("002")

    parking_001.park_car(car_a)
    parking_002.park_car(car_b)


if __name__ == "__main__":
    main()
