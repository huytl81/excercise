class Person:
    _count = 0  # Class variable (class attribute) to keep track of the number of Person instances

    # constructor
    def __init__(self,name, age):
        self.__name = name # Instance variable (instance attribute)
        self.age = age
        Person._count += 1
    
    def greeting(self):
        print(f"Welcome {self.__name} to my world! You are {self.age} years old, right?")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


# Create instances of the Person class
person_1 = Person("Alice", 30)
person_1.set_name("Huy Ta")

print(person_1.get_name()) # person_1.get_name()

Person._count = 100
print(f"Total number of persons we have: {Person._count}")

# Accessing instance attributes
print(f"Person 1 name: {person_1._Person__name}")