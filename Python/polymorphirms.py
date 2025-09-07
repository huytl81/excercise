# class Animal():
#     def __init__(self):
#         pass
#     def speak(self):
#         print("Animal is speking")
    
# class Dog(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f"{self.name} is speaking")

# class Cat(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f"{self.name} is speaking")

# my_animal = Animal()
# my_dog = Dog("Vang", 2)
# my_cat = Cat("Miu", 1)

# my_animal.speak()
# my_cat.speak()
# my_dog.speak()

# duck typing, as long as cat has speak method
#def shout(dog):dog.speak()
# def shout(dog: Dog): 
#     if not isinstance(dog, Dog):
#         raise TypeError("Expected a Dog instance")
#     dog.speak()

# shout(my_cat)
# shout(my_dog)

""" inheritance multiple level """
# class Ong:
#     def showOng(self):
#         print("Ong")
    
#     def demo(self):
#         print("demo Ong")

# class Cha(Ong):
#     def showCha(self):
#         print("Cha")

#     def demo(self):
#         print("demo Cha")
# class Con(Cha):
#     def showCon(self):
#         print("Con")

# con = Con()
# con.showCha()
# con.showOng()
# con.demo()

""" multilpe inheritance """

class Ong:
    def showOng(self):
        print("Ong")
    
    def demo(self):
        print("demo Ong")

class Cha:
    def showCha(self):
        print("Cha")

    def demo(self):
        print("demo Cha")
class Con(Ong, Cha): # theo thu tu
    def showCon(self):
        print("Con")

con = Con()
con.demo()