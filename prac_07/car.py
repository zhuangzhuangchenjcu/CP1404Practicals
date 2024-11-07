"""
CP1404 Practical
Car class
Author: CHENZHUANGZHUANG
"""


class Car:

    def __init__(self, name="", fuel=0):
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount):
        self.fuel += amount

    def drive(self, distance):
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance