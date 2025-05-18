#Addition

def add(x, y):
    result = x + y
    print(f"The sum of {x} and {y} is {result}")

#Subtraction
def subtract(x,y):
    result = x-y
    print(f"The difference between {x} and {y} is {result}")

#Multiplication
def multiply(x,y):
    result = x*y
    print(f"The product of {x} and {y} is {result}")

#Division
def divide(x,y):
    try:
        result = x / y
        print(f"The quotient of {x} and {y} is {result}")
    except ZeroDivisionError:
        print("Oops! Division by zero is not allowed.")

#Menu choices
try:
    menu = int(input("Choose one of the following operations! \n" 
    "1. Addition \n" 
    "2. Subtraction \n"
    "3. Multiplication \n"
    "4. Division \n"
    "5. Exit \n"))

    if menu == 5:
        print("Goodbye!")
    elif (menu == 1 or 2 or 3 or 4):
        try:
            numb1 = float(input("Enter the first number: "))
            numb2 = float(input("Enter the second number: "))

            if menu == 1: # Call to addition function
                add(numb1,numb2)
            elif menu == 2: # Call to subtraction function
                subtract(numb1,numb2)
            elif menu == 3: # Call to multiplication function
                multiply(numb1,numb2)
            elif menu == 4: # Call to division function
                divide(numb1,numb2)

        except ValueError:
            print("Please enter a valid number.") # if input is anything but a float
        
    else:
        print("Invalid choice, please pick again") # if choices don't exist
        
except ValueError:
    print("Invalid input! Please enter a number for the menu option.") # # if choices don't exist
