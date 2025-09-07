

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod # bat buoc phai implement o class con
    def sound(self):
        pass
    def run(self):
        print("speed up...")

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"
    pass


# my_animal = Animal() # This will raise an error because we cannot instantiate an abstract class
my_dog = Dog()
print(my_dog.sound())
print(my_dog.run())
