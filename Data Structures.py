# LIST
# Declaration - []
# We can modify the list items
names = ['Cersci', 'Jaime', 'Tyrion','Robb','John Snow']
print(names)
print(names[3])
print(names[-1])
print(names[1:-2])
names[0] = 'Joffrey'  # This will replace the first item 
print(names)

# Exercise 
numb = [12,45,37,5,554,342,34,76,976,32,45]
max = 0
for i in numb:
    if i > max:
        max = i
print(max)

###############################################################################

# 2D Lists
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
    ]
print(matrix[0][1]) # will print second element of first list
for row in matrix:
    for item in row:
        print(item) # This nested loop will return all the elements of the list

###############################################################################      

#  List Methods
# Operations we can perform on list
numbers = [1,3,4,6,76,87,9,0,3,223,235,9,9,9]
numbers.append(45) # will add value at last
numbers.insert(3, 365) # will take index and vaue, this will insert value in the given index
numbers.remove(76) # Will Remove the value entered 
numbers.pop() # will remove last item in a list
print(numbers.index(87)) # will return the index value in the list 
print(9 in numbers) # Will return True if number is in the list
print(numbers.count(9)) # will print the number of 9s present in the list
numbers.sort() # will sort the list
print(numbers)
numbers.reverse() # will reverse the list
print(numbers)
numbers2 = numbers.copy()  # Make a copy of our list
print(numbers2)
numbers.clear()  # Empty the list
print(numbers)
 
# List Operations Exercise (Removing the duplicates)
list1 = [12,13,45,67,89,9,13,89,45,46,45,12]
list2 = []
for i in list1:
    if (i in list2):
        None
    else:
        list2.append(i)
print(list1)
print(list2)

###############################################################################

# Tuples
# Declaration - ()
# Similar to list, But they are un-changable
tuple1 = (1,2,3,3,3,3,3,3,4,5,6,7,8)
print(tuple1[0])
print(tuple1.count(3)) # To count the number of 3s
print(tuple1.index(7)) # To return the index of value entered

###############################################################################

# Unpacking 
# To reduce the number of times we wnter values and store it in varaibles
# not limited to tuple, can use in list as well
coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x,y,z = coordinates  # The same thing from lines 80 to 83 achieved here # UNPACKING

###############################################################################

# Dictinaries 
#  Key value pairs, Keys are unique
# Declaration - {}
Library1 = {
    "Name":"Yashwanth",
    "Roll_No":"19BLC1043",
    "DOB":"May 27,2002"
    }

print(Library1["Name"])  # Will return value when we pass key, Also will rteurn error if key not in dictionary
print(Library1.get("NameABCD")) # Will not throw an error even if key not in dictionary
print(Library1.get("NameABCD", "John Snow")) # Will return default value entered ("John snow in this case") if key not given
Library1["Name"] = "Aegon Targaryen" # This will update the dictionary
print(Library1.get("Name"))

# Exercise
numbers1 = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
    }
ab=input("Phone: ")
final = ''
for i in ab:
    final+= (numbers1.get(i, '!') + ' ')
print(final)

###############################################################################

# Emoji Convertor 
message = input("> ")
words = message.split(' ') # Split method will seperate entire string based in value entered in brackets (In this case its space)
print(words)
emojis={
        ':)': '😊',      # Windows + .(period) for emojis in win11
        ':(': '😔',
        'cry': '😭',
        'love': '💕'
        }
final = ''
for i in words:
    final += (emojis.get(i,i) + " ")
print(final)