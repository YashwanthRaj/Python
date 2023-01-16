# Classes
# We use classes to define new types
# Always name the class with first Letter Capital and variable and function names all small letters 
# Class - defines the blueprint/template for creating object  || Object - Actual instances based on blueprint

class Points:       # Defining class
    def draw(self):      # Some functions inside the class, and every function inside class should have self as parameter
        print("Draw")
    def line(self):
        print("Line")

point1 = Points()       # creating an object point1
point1.draw()           # Now we can see that all the functions defined inside the class are accessable by the object
point1.line()

point1.x = 23        # here we are specifying an attribute particular to this object
print(point1.x)

###############################################################################

# Constructors 
# Constructor is a function that gets called at the time of creating an object 
# definition, a constructor defineda d=s a function inside class
# __init__ -> short for initialise 

class Points:       # Defining class
    def __init__(self, x, y):             # Constructor
        self.x = x
        self.y = y
    def draw(self):      # Some functions inside the class
        print("Draw")
    def line(self):
        print("Line")
point1 = Points(15, 30)
print(point1.x)

# Exercise
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi I am {self.name}, I am Talkative")
name1 = Person("Sansa")
print(name1.name)
name1.talk()
name2 = Person("Bob")
name2.talk()

###############################################################################

# Inheritance
# A mechanism for reusing code

class Mammal:
    def walk(self):
        print("Walk")
    def pee(self):
        print("I gotta pee")


class Dog(Mammal):             # We define parent class inside brackets
    pass    # This is to prevent empty class error


class Cat(Mammal):
    def meow(self):
        print("I am a cat")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.pee() 
cat1.meow()
