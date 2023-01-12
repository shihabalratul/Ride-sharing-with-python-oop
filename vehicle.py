from abc import ABC, abstractmethod
from time import sleep
from turtle import distance

class Vehicle:
    speed = {
        "car": 30,
        "bike": 50,
        "cng": 15
    }
    def __init__(self, vehicle_type,license_plate, rate, driver) -> None:
        self.vehicle_type = vehicle_type
        self.rate = rate
        self.driver = driver
        self.license_plate = license_plate
        self.speed = self.speed[vehicle_type]
        self.status = "available"

    @abstractmethod
    def start_driving(self):
        pass

    @abstractmethod
    def trip_finished(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type,license_plate, rate, driver)
    
    def start_driving(self, start, destination):
        self.status = "unavailable"
        print(self.vehicle_type, self.license_plate, "Started")
        distance = abs(start-destination)
        for i in range(0, distance):
            sleep(.5)
            print(f"Driving: {self.license_plate} current position: {i} of {distance}\n")
    
    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "Completed Trip")
    
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type,license_plate, rate, driver)
    
    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type, self.license_plate, "Started")
        
    def start_driving(self, start, destination):
        self.status = "unavailable"
        print(self.vehicle_type, self.license_plate, "Started")
        distance = abs(start-destination)
        for i in range(0, distance):
            sleep(.5)
            print(f"Driving: {self.license_plate} current position: {i} of {distance}\n")
    
    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "Completed Trip")
    
class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        super().__init__(vehicle_type,license_plate, rate, driver)
    
    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type, self.license_plate, "Started")
    
    def start_driving(self, start, destination):
        self.status = "unavailable"
        print(self.vehicle_type, self.license_plate, "Started")
        distance = abs(start-destination)
        for i in range(0, distance):
            sleep(.5)
            print(f"Driving: {self.license_plate} current position: {i} of {distance}\n")
    
    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "Completed Trip")
    
