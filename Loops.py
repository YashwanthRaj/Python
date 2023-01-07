# IF ELSE conditional statements
# If the given condition is true, then it willl execute, or it will come out and move on to next one 
is_hot = False
is_cold = True
if is_hot:
    print("It is warm outside")
    print("Wear cotton clothes")
elif is_cold:
    print("It is cold outside")
    print("Wear wollen clothes")
else:
    print("It is neither hot nor cold")
print("Have a lovely day")

# Exercise
price = 1000000
down_payment=0
good_credit=bool(input("Enter if buyer has good credit (T/F): "))
if good_credit:
    down_payment=(10/100)*price
    message = f'Your payable amount is 10% which is {down_payment} Dollors'
    print(message)
else:
    down_payment=(20/100)*price
    message = f'Your payable amount is 10% which is {down_payment} Dollors'
    print(message)

###############################################################################

# Logical Operator
has_good_credit = True
has_good_record = False
if has_good_credit and has_good_record:  # AND both conditions must be true
    print("You are clear!!")
elif has_good_credit or has_good_record: # OR means one true is enough
    print("We can work things out!!")
else:
    print(" You are barred from work ")

criminal_record = False
if not criminal_record:
    print("You are fine to go")  # NOT will reverse the condition

###############################################################################

# Comparison Operator
temperature = 50
if temperature > 45:  # Other operators like >= ; <= ; > ; < 
    print("It is hotter!!")
else:
    print("Temperature is colder")
    
if temperature == 55:  # Equality checking operator: Single equality operator is to assign the value
    print("Equal")
elif temperature != 45:  # Not equal to operator
    print("Not 45")

# Exercise
name = input("Enetr your name: ")
len_name = len(name)
if len_name < 3:
    print("Your name must be minimum 3 characters long!!")
elif len_name > 50:
    print("Your name must have maximum of 50 characters!!")
else:
    print(f'Welcome {name}! Have a nice day')

###############################################################################

# Mni Project - Weight Convertor 
weight = float(input("Enter your weight: "))
nweight = 0
Unit = input("(K) for kiogram and (L) for pounds: ")
Unit = Unit.lower()
if Unit == 'l':
    nweight = 0.453592*weight
    print(f"Your Weight in Kilograms is: {nweight}")
elif Unit == 'k':
    nweight = weight/0.453592
    print(f"Your Weight in pounds is: {nweight}")
else:
    print("Please enter a valid input for Unit of weight")

###############################################################################

# While Loops
# Used when we want to execute a block of code repeatedly until a condition is met, 
# but make sure to add increment or decrement operator ot it will be infinite loop
# Like if, while loops can also have else part
i = 1
while i<10:   # This loop keeps running umtil condition is false
    print(('*')*i)
    i+=1
print("Done")

#Guessing Game using While Loop
sec_num = 5
i=3
while i>0:
    your_num = int(input("Enter your guess: "))
    i-=1
    if sec_num == your_num:
        print("Yay!! You guesses it right")
        break
    else:
        print(f"Try Again!!, you have {i} attempts remaining")
else:
    print("Sorry! You have exhausted all your tris!! :(")
    
###############################################################################

# Car Game  
print("Welcomr to car game!!")
cmd = ''
status = False
while True:
    cmd = input("> ").lower()
    if cmd == "help":
        print('''
Start - To start your car engine
Stop - To stop your engine
Quit - To quit the game!
              ''')
    elif cmd == 'start':
        if status:
            print("Car is already ON!")
        else:
            print("Engine ON.... Ready to go......")
            status = True
    elif cmd == 'stop':
        if status:
            print("Engine turned OFF....")
            status = False
        else:
            print("Car is already OFF!!")
    elif cmd == "quit":
        print("The END")
        break
    else:
        print("Cannot Understand :(")
 
###############################################################################

# FOR LOOPS
# We use them to iterate over collection 
for i in 'python': # Iterate over string
    print(i)
for j in ["Tyrion Lannister","Cersei Lannister","Jaime Lannister"]: # Iterate over list
    print(j)

for m in range(5,50,5):  # range(start, stop, step/iteration)
    print(m)
    
# Exercise
items = [10,20,30,40,50,60,70,80,90]
tot_cost = 0
for i in items:
    tot_cost+=i
print(f"The total cost is: {tot_cost}")

###############################################################################

# Nested Loops
# Adding one loop inside of another loop
for x in range(5):
    for y in range(5):
        print(f"({x}, {y})")

# Exercise
val = [5,2,5,2,2]
for i in val:
    ab = ''
    for j in range(i):
        ab+='x'
    print(ab)