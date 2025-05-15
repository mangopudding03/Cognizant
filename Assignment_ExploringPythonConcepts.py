
# Task 1
print('Task 1 \n')
name = "Maanya" # My name
age = 22 # My age
height = 5.5 # My height

print(f"Hey there, my name is {name}! I’m {age} years old and {height} feet tall.") # My intro message

# Task 2 
print('Task 2 \n')
num1 = 1
num2 = 1

# Addition
print("The sum of", num1, "and", num2, "is", num1 + num2) #Add num1 and num2

# Subtraction
print("The difference between", num1, "and", num2, "is", num1 - num2) #Subtract num 1 by num2

# Multiplication
print("Multiplying", num1, "and", num2, "gives", num1 * num2) #Multiply num 1 and num2

# Division
print("Dividing", num1, "by", num2, "gives", num1 / num2) #Divide num 1 with num2


# Task 3
print('Task 3 \n')
user_input = input("Enter a number: ")

number = float(user_input) # in case of a decimal, float is necessary 

if number > 0:
    print("This number is positive.") # If a number is greater than 0, its positive
elif number < 0:
    print("This number is negative.") # If a number is less than 0, its negative
else:
    print("It's a zero")


