print("Hello World")  # Prints whatever is inside the brackets
print("Yash" * 10) # Prints the string 10 times

###############################################################################

# VARIABLES - We use variables to temporarily store data 
var1 = 10  # int
var2 = 4.9 # decimal
var3 = "String Variable" # String
var4 = False # Boolean 
print(var1)

# Variable exercise
name = "John"
age = 20
new_patient = True
print(name,age,new_patient)

###############################################################################

# Getting Input
name = input("What is your name?")  # By default it will take input as string
print("Hi " + name)

# Geting input exercise
name1 = input("Hi what is your name? ")
color = input("Hi "+name1+" , What color do you like? ")
print(name1+ " likes "+color)

###############################################################################

# Type conversion
Yage = int(input("What year were you born? "))
age = 2022 - Yage
print(age)
print(type(age)) # Prints the type of variable

# Type conversion Exercise
weight = input("Enter your weight in pounds: ")
weightKG = 0.453592*float(weight)
print(weightKG)
print(type(weightKG))

###############################################################################

# Strings
para1 = '''
Hi My name is Yashwanth
Very nice to meet you all
'''
print(type(para1))
print(para1)

nameA = 'My Name is Yashwanth'
print(nameA[0])  # Indicates the first letter/Character , 1 means 2nd one from  begining
print(nameA[-1]) # Indicates the last letter/Character , -2 means second one from end
print(nameA[0:6]) # Prints first to 6th position, includes index 0, excludes index 6
print(nameA[5:]) # from index 5 till last
print(nameA[:9]) # first to index 8 
nameB = nameA[:] # [:] copies entire string 
print(nameB)

###############################################################################

# Formatted Strings
first_name = "Yashwanth"
last_name = "Raj"
message = first_name + ' ['+last_name+'] is a coder'
message1 = f'{first_name} [{last_name}] is a coder'  # Defined as F'' here anything in {} is a string
print(message)
print(message1)

###############################################################################

# String methods
name='Yashwanth'
print(len(name))  # len returns the length of string 

# When  function is specific to that object, we call it as method
print(name.upper())  # this method does not change or modify the original string
print(name.lower())
print(name.title()) # returns the string where first character in every word is Upper case
print(name.find('s')) # this will return the index of entered character, will return -1 if object not there
print(name.find('nth'))  # we can also pass a series of string
print(name.replace("nth", "raj"))
print('Yash' in name) # in will return boolean if the given string is in the given variable 

###############################################################################

# Arthmetic Operations
print(10 + 3) # Addition
print(10 - 3) # Subtraction
print(10 * 3) # Multiplication
print(10 / 3) # Division but return float values
print(10 // 3) # Division but return int values
print(10 % 3) # will return remainder
print(10 ** 3) # Exponents

# Augmented Assignment Operater
x=15
x+=2 # Adds 2
print(x)
# Operator Precedence (Order of operations) BODMAS
 
###############################################################################

# Math Functions
x=2.9
print(round(x)) # Rounds the number to nearest Integer
print(abs(-20.654)) # abs short for Absolute, returns +ve 

# To do complex mathematical functions, import math module 
import math # importing math module
print(math.ceil(4.8)) # Return cieling of an integer
print(math.floor(50.85)) # return floor of an Integer 