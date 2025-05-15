# Voter Eligibility

age = int(input("How old are you? ")) #getting the user's age

if age >= 18: #Legal age to vote
    print("Congratulations! You are eligible to vote. Go make a difference!") #Letting them know they can vote
else:
    years_left = 18 - age
    #Letting them know they're ineligible and the amount of years they still have left to be able to vote
    print(f"Oops! You're not eligible yet. But hey, only {years_left} more year{'s' if years_left > 1 else ''} to gooooo!")

