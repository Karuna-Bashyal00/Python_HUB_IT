
# note: Private Member & Protected Member
# class Employee:
#     def __init__(self):
#         self._name = "Dipen"
#         self.__salary = 3000 

# class EmployeeChild(Employee):
#     def __init__(self):
#         Employee.__init__(self)
#         print("Calling Parent Class")
#         return(self.__salary)

# object1 = EmployeeChild()
# print(object1._name)

# note: Accessing private data & protected data
class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        self.__display_salary()
    
    def __display_salary(self):
        print(f"Salary: {self.__salary}")
        
person = Person('Karuna',19,100)

# print(person.name)
# print(person._age)
# print(person.__salary)

# ?name mangling method
print(person._Person__salary)

# person.display_details()