
# todo: Single Inheritance
# class Father():
#     def eat(self):
#         print("Father eats Banana")
        
#     def walk(self):
#         print("Father walks")
        
# class Child(Father):
#     def eats(self):
#         print("Child eats Apple")

# child1 = Child()

# child1.eat()
# child1.walk()
# child1.eats()

# note: Multiple Inheritance
# *Parent Class
# class Father():
#     father_Name = ""
#     def father(self):
#         print(self.father_Name)

# *Parent Class
# class Mother():
#     mother_Name = ""
#     def mother(self):
#         print(self.mother_Name)

# *Child Class
# class Son(Father, Mother):
#     def __init__(self, name='virat'):
#         self.name = name
#         print("Son's Name is: ", self.name)
        
#     def details(self):
#         print("Father's Name is: ", self.father_Name)
#         print("Mother's Name is: ", self.mother_Name)

# !(object-name) = (Child_class())
# son1 = Son()
# son1.father_Name = "Ravi"
# son1.mother_Name = "Rani"
# son1.details()

# note: Multilevel Inheritance
class GrandFather():
    pass

class Father(GrandFather):
    pass

class Child(Father):
    pass
