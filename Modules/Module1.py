# Modules
# Modules in python are basically some python code and we use to organize our code into multiple files
# We break our complete code into different files called modules

import Mod1Functions           # Importing functions from Mod1Functions file
from Mod1Functions import Kg_to_lbs  # Importing specific function from that module

weight1 = int(input("Enter the weight: "))
metric = input("Enter KG or LBS: ").lower()
if metric == 'kg':
    ans = Mod1Functions.Kg_to_lbs(weight1)  # Acessing functions form Mod1Functions
    print(ans)
elif metric == 'lbs':
    ans1 = Mod1Functions.Lbs_to_Kg(weight1)
    print(ans1)
else:
    print("Cannot understand that!!")

###############################################################################

# Exercise 
from Mod1Functions import MaxNum

list1 = [10,20,30,40,50,60,78,56,64,516,6]
ab = MaxNum(list1) # Because we called the specific function from module Mod1Functions, we dont need to specifiy the mod name 
print(ab)

###############################################################################

# Packages
# Another way to organize the code
# Its a container for multiple modules  
# Create a direcotory in python, add file name __init__.py - This will be considered as package by python 

# importing a package with modules inside other tnah __init__ Syntax below
# import package_name.module_name

# Acessing the module - package_name.module_name.function_name()

# Here too we can do from ____ import ____ to save time
# You can either import module from package and use package object to access the functions, or import function itself 

# There are a lot of inbuilt packages for python 

###############################################################################

# Generating random values with Inbuilt Package

import random # importing random package

for i in range(3):
    print(random.random())    # Gives out random values
    print(random.randint(4,45))  # Gives random values between the two numbers mentioned 

members = ['Harry', 'Jaime', 'Wednesday', 'Randy']
print(random.choice(members)) # Prints random from given list

# Exercise
A = input("Enter Y or N!!: ").lower()
if A == 'y':
    print(random.randint(1,6))
elif A == 'n':
    print("Ok Exit")
else:
    print("Cannot Understand that!!")

###############################################################################

# pypi - Python Package Index
# Here we can find a lot of packages 