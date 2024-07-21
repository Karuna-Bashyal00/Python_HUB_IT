
# note: Method Overriding in Polymorphism
# class Animal():
#     def sound(self):
#         print("Parent makes a sound.")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks.")

# dog = Dog()
# dog.sound()

# note: Polymorphism in Inheritance
# class Shape:
#     def draw(self):
#         pass
#         # raise NotImplementedError("Parent class ma kei lekhna paidaina.")
    
# class Circle(Shape):
#     def draw(self):
#         print("Drawing a circle.")
        
# class Square(Shape):
#     def draw(self):
#         print("Drawing a square.")

# class Rectangle(Shape):
#     def draw(self):
#         print("Drawing a rectangle.")

# shapes = [Circle(), Square(), Rectangle()]

# for shape in shapes:
#     shape.draw()

# note: Use of Polymorphism with function using loop
# def make_sound(animal):
#     return animal.sound()

# class Cat:
#     def sound(self):
#         return "Meow!"
    
# class Dog:
#     def sound(self):
#         return "Bhou Bhou!"

# animals = [Dog(), Cat()]

# for animal in animals:
#     print(make_sound(animal))

# note: Use of polymorphism without loop in Function
class Nepal():
    def language(self):
        print ("Nepali")
    
    def currency(self):
        print ("Rupaiya")

class India():
    def language(self):
        print ("Hindi")
    
    def currency(self):
        print ("Rupees")
    
class China():
    def language(self):
        print ("Chinese")

    def currency(self):
        print ("Yuan")

def details(object):
    object.language()
    object.currency()

object_nepal = Nepal()
object_india = India()
object_china = China()

details(object_nepal)
details(object_india)
details(object_china)

