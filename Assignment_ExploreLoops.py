# Task 1 
print('Task 1')
start = int(input("Enter the starting number: "))

while start > 0:
    print(start, end=" ")
    start -= 1
print("Blast off! \n")


# Task 2
print('\n Task 2')
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()


# Task 3 
print('Task 3')
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}.")


