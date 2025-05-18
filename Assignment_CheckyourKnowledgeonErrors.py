# Task 1

print("Task 1")
try:
    numin = int(input("Enter a number: "))
    result = 100/numin
except ZeroDivisionError: # Zero division error
    print("Oops! You cannot divide by zero.")
except ValueError: # Invalid value error
    print("Invalid input! Please enter a valid number")
else:
    print(f"100 divided by {numin} is {result}")

# Task 2

print("\n Task 2")
try:
    exinput = int(input("Enter list index: "))
    exlist = [10,20,30,40,50] # creating a list full of indexes to have a range of accessible indexes
    print(exlist[exinput])
    
except IndexError: # Index error
    print("IndexError occurred! List index out of range.")

try:
    exinput = input("Enter key: ")
    exdict = {"name": "Maanya", "age": 22} # creating a dict with a couple keyt value pairs to have a range of accessible keys
    print(exdict[exinput])
    
except KeyError: # Key error
    print("KeyError occurred! Key not found in the dictionary")

try:
    exinput = input("Enter value: ") # errors out with everything because input is not an integer
    opp = 5 + exinput
    print(opp)
    
except TypeError: #Type error
    print("TypeError occurred! Unsupported operand types.")


# Task 3
print("\n Task 3")
#Attempt division block
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: ") ) 
    result = num1/num2
#Exceptions
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number")
#Result
else:
    print(f"The result is {result}")
#Final message
finally:
    print("This block always executes")