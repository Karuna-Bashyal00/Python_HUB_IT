
# note: Single Inheritance
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

# ?(object-name) = (Child_class())
# son1 = Son()
# son1.father_Name = "Ravi"
# son1.mother_Name = "Rani"
# son1.details()

# note: Multilevel Inheritance
# class GrandFather():
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername

# class Father(GrandFather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
        
#         GrandFather.__init__(self, grandfathername)
    
# class Daughter(Father):
#     def __init__(self, daughtername, fathername, grandfathername):
#         self.daughtername = daughtername
        
#         Father.__init__(self, fathername, grandfathername)
        
#     def print_details(self):
#         print("Grandfather name :", self.grandfathername)
#         print("Father name :" + self.fathername)
#         print("Daughter name :" + self.daughtername)

# daughter1 = Daughter('deepsikha', 'dipendra', 'dinesh')
# print(daughter1.grandfathername)
# daughter1.print_details()

# note: Hierarchical Inheritance
class ParentClasss():
    def food1(self):
        print("ParentClass Food is Chowmein.")

class Child1(ParentClasss):
    def food2(self):
        print("Child1 Food is Burger.")

class Child2(ParentClasss):
    def food3(self):
        print("Child2 Food is Pizza.")

children1 = Child1()
children2 = Child2()

print("--------Child1-----------")
children1.food1()
children1.food2()

print("--------Child2-----------")
children2.food1()
children2.food3()   

     



