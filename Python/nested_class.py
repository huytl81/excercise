# class Car:
#     class Engine:
#         def __init__(self, hp):
#             self.hp = hp

#         def start(self):
#             print(f"Engine {self.hp} is starting...")

#     def __init__(self, brand, hp):
#         self.brand = brand
#         self.engine = self.Engine(hp)
    

# my_car = Car("Mitsubishi", 200)
# print(my_car.brand)
# my_car.engine.start()

class University:
    class Department:
        def __init__(self, name, head):
            self.name = name
            self.head = head
        def list_students(self):
            return ("Huy Ta", "Sen Thoi", "Huy Ha")

    def __init__(self, name):
        self.name = name
        self.departments = []
    def __str__(self):
        return f"{self.name}"
    def add_department(self, department):
        self.departments.append(department)

    def list_departments(self):
        for department in self.departments:
            print(f"Department: {department.name}, Head: {department.head}")

university = University("Demo University")
cs_dept = university.Department("Computer Science", "Prof. John")
math_dept = university.Department("Mathematics", "Prof. Jane")

university.add_department(cs_dept)
university.add_department(math_dept)

print(university)
university.list_departments()
print(cs_dept.list_students())

