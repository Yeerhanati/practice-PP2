# Class variables vs instance variables
class Car:
    wheels = 4  # Class variable

    def __init__(self, color):
        self.color = color  # Instance variable

car1 = Car("red")
car2 = Car("blue")

print(car1.color, car1.wheels)
print(car2.color, car2.wheels)