# We are creating this module with two functions which we will use from main Module1 file 

def Kg_to_lbs(weight):
    return weight / 0.45

def Lbs_to_Kg(weight):
    return weight * 0.45

def MaxNum(numbers):
    max1 = numbers[0]
    for number in numbers:
        if number > max1:
            max1 = number
    return max1