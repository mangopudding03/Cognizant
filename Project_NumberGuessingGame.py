import random

print("Guess the number (between 1 and 100): ")
# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)


attempts = 0
max_attempts = 10 # max attempts

# The loop
while attempts < max_attempts:
    guess = int(input(f"\n Guess the number (Attempt {attempts + 1}/{max_attempts}): "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempt{'s' if attempts > 1 else ''}!")
        break
else:
    print(f"\n Game over! The number was {number_to_guess}. Better luck next time!")