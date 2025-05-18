# Task 1
print("\n Task 1")
def addNumbers(a,b): # Sum of a and b
    return a + b

def greet_user(name, a, b):
    result = addNumbers(a,b) # Calls function addNumbers
    print(f"Hello, {name}! The sum of {a} and {b} is {result}") # Prints the output

greet_user('Maanya' , 5 , 10) # The name and a and b

# Task 2
print("\n Task 2")

def describePet(pet_name , pet_name2, animal_type2, animal_type = "dog"): #default type is dog
    print(f"I have a {animal_type} named {pet_name}. I have a {animal_type2} named {pet_name2}.")

describePet("Buddy","Whiskers", "cat") # you don't have to write dog

# Task 3
print("\n Task 3")
def makeSandwich(*ingredients): #positional argument
    print(f"Making a sandwich with the following ingredients:", end=" ")
    for ing in ingredients:
        print(f"- {ing}", end= " ")
makeSandwich("Lettuce", "Tomato","Cheese", "Buns") #Ingredients

# Task 4
print("\n Task 4")

def factorial(a):
    if a == 0 or a ==1:
        return 1
    else:
        return( a * factorial(a - 1))

def fibonacci(a):
    if a<=0:
        return 0
    if a == 1:
        return 1
    return(fibonacci(a-1) + fibonacci(a-2))

factorialnum = factorial(5)
fibonaccinum = fibonacci(6)

print(f"Factorial of 5 is {factorialnum}. The 6th Fibonacci number is {fibonaccinum}.")