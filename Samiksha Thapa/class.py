class animal:
    work1 = "bark"
    def __init__(self, name, food, work):
        self.name = name
        self.food = food
        self.work = work
        print (f'{name} + {work}')
    
    def view_details(self):
        
        print(self.name + ' ' + self.food + ' ' + self.work)
    
# Creating objects of class animal

# (object_name) = (class_name(parameters value))
ani1 = animal('dog', 'pasta', 'bark')
ani2 = animal('cat', 'noodles', "meow")

ani1.view_details()
ani2.view_details()

# Calling class value directly
print(animal.work1)
