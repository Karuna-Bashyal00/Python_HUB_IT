class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age += 1
    
    def display(self, context=""):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Subu", 21)
person1.display("before birthday: ")  
person1.birthday()

person1.display("after birthday: ")  