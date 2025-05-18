try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: ") ) 
    result = num1/num2
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number")
else:
    print(f"The result is {result}")
finally:
    print("Byeeee")