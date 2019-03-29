class Car:
    def move(self):
        print("Car is moving.....")

class Bike:
    def move(self):
        print("Bike is moving.....")

class Bicycle:
    def move(self):
        print("Bicycle is moving.....")

class Vehicle:
    def setVehicle(self,obj):
        obj.move()

v1 = Vehicle()
v1.setVehicle(Bicycle())
v1.setVehicle(Car())
v1.setVehicle(Bike())
