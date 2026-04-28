# Method overriding in child class
class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

cat = Cat()
cat.speak()