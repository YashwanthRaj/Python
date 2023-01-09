# Functions
# A container for a few lines of code that perform a specific task

def greet_user():       # Function definition
    print("Hello User!!")
    print("Welcome Aboard.....")

print("Start")
greet_user()   # Calling the function, Always call the function after you define it
print("Finish")

###############################################################################

# Parameters
def greet_user(name):      # name passed as parameter
    print(f"Hello {name}")
    print("Welcome Aboard.....")

name1= input("Enter the name: ")
greet_user(name1)   
greet_user("Tyrion")

def name1(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print(f"Your last name is: {last_name}")

name1("Yashwanth", "Raj")  # Positional Arguemntm without any keys in parameter

###############################################################################

# Key Word Arguements
# During the parameter definition, we can specify the position intended

def name2(f_name,l_name):
    print(f"Hello {f_name} {l_name}")
    print(f"Your last name is: {l_name}")

name2(f_name="Tyrion", l_name="Lannister") # Keyword Arguement, here we specify the position of Parameter
name2(f_name"Jaime","Lannister") # This is not good as positional arguement should never be after keyword arguement
name2("Jaime",l_name"Lannister") # This is correct as keyword arguement is after positional 

###############################################################################

# Return Statement 
def square(numb):
    return numb*numb  # This statement will return the value operation

numb1 = int(input("Enter the number: "))
square1 = square(numb1)
print(f'The square is {square1}')
print(square(12))  # Also works with print directly

###############################################################################

# Creating a reusable function
# A general rule of thumb for functions are that, they should not concern with getting input or output
def emoji_recv(message):
    words = message.split(' ') 
    emojis={
            ':)': '😊',      # Windows + .(period) for emojis in win11
            ':(': '😔',
            'cry': '😭',
            'love': '💕'
            }
    final = ''
    for i in words:
        final += (emojis.get(i,i) + " ")
    return final
        
message = input("> ")
print(emoji_recv(message))

###############################################################################

# Exceptions
# In the output terminal window, exit code 0 means program workking without any error
# In the output terminal window, exit code anything but 0, means program has errors

try:                    # This will try the first block of code, if returns error, then will go to except
    age = int(input("Enter the number: "))
    income = 20000
    risk=income/age
    print(age)
except ValueError:       # This block of code will run when the above code encounters an ValueError
    print("Not an Integer")
except ZeroDivisionError:   # This block of code will run when the above code encounters an ValueError
    print("Age cannot be zero")