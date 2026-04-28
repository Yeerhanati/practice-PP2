# Use super() to call parent class constructor
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Buddy", "Husky")
print(dog.name, dog.breed)