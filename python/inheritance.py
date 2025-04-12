class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

dog = Dog()
dog.sound()  # Output: "Woof!"
class Cat(Animal):
    def sound(self):
        print("Meow!")

cat = Cat()
cat.sound()  # Output: "Meow!"