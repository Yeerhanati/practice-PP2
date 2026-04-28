# Instance methods with self
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

p1 = Person("Charlie")
p1.introduce()