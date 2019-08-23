import os
import csv
import tempfile


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = "car"
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.car_type = "truck"
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        if body_whl:
            dimentions = body_whl.split("x")
            self.body_length = float(dimentions[0])
            self.body_width = float(dimentions[1])
            self.body_height = float(dimentions[2])
        else:
            self.body_length = self.body_height = self.body_width = None

    def get_body_volume(self):
        try:
            return self.body_height * self.body_width * self.body_length
        except TypeError:
            print("Unknown body dimensions")


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = "spec_machine"
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            vehicle = ', '.join(row).split(";")
            if vehicle[0] == "":
                continue

            if vehicle[0] == "car":
                if vehicle[1] and vehicle[2] and vehicle[3] and vehicle[5]:
                    car = Car(vehicle[1], vehicle[3], float(vehicle[5]), int(vehicle[2]))
                    car_list.append(car)
                else:
                    continue

            elif vehicle[0] == "truck":
                if vehicle[1] and vehicle[3] and vehicle[5]:
                    truck = Truck(vehicle[1], vehicle[3], float(vehicle[5]), vehicle[4])
                    car_list.append(truck)
                else:
                    continue

            elif vehicle[0] == "spec_machine":
                if vehicle[1] and vehicle[3] and vehicle[5] and vehicle[6]:
                    spec_machine = SpecMachine(vehicle[1], vehicle[3], float(vehicle[5]), vehicle[6])
                    car_list.append(spec_machine)
                else:
                    continue

            else:
                print("Incorrect vehicle type")
    return car_list

#scania = Truck("Scania", "photo.png", 30, "12x6x2.5")
#print(scania.get_body_volume())
#print(get_car_list("cars.csv")[2].get_body_volume())