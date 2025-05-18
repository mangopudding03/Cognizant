# Function for adding expenses
def addexpenses(cdict):
    description = input("Enter Expense description: \n")
    if description == '':
        print("Description cannot be empty.") # Exception error if description is empty
        return
    category = input("Enter Category: \n")
    if not category:
        print("Category cannot be empty.") # Exception error if category is empty
        return
    try:
        amount = float(input("Enter amount: \n")) # amount in float 
    except ValueError:
        print("Invalid amount. Please enter a number.") # incase amount isn't a float, exception error
        return
    expense = (description, amount) # tuple
    if category not in cdict: 
        cdict[category] = []
    cdict[category].append(expense)
    print("Expense added successfully") # Added successfully!


def vexpenses(cdict):
    if not cdict:
        print("No expenses recorded yet.\n") # Incase no expense was recorded
        return
    print("Expenses \n")
    for category, expenses in cdict.items():
        print(f"Category: {category}")
        for description,amount in expenses: # Unpack tuple
            print(f"  - {description}: ${amount:.2f}")
    print()

def vsummary(cdict): # Incase no expense was recorded so summary is empty
    if not cdict:
        print("No expenses to show.\n")
        return
    print("Summary:")
    for category, expenses in cdict.items(): # each category iteration
        # sum of all amounts inside expenses
        total = 0
        for description,amount in expenses: # Unpack tuple
            total += amount # Sum of all amounts in the category
        print(f"{category}: ${total:.2f}")
    print()

def main():

    print("Welcome to the Personal Finance Tracker! \n") # Welcome message
    cdict = {} #Empty dict

    while True:
        try:
             # Menu of choices 
            menuofchoices = int(input("What would you like to do? \n"
            "1. Add Expense \n"
            "2. View All Expenses \n"
            "3. View Summary \n"
            "4. Exit \n"))
        except ValueError:
            print("Please enter a valid number between 1 and 4.\n")
            continue
        
        # Map functions to the menu of choices 
        if menuofchoices == 1:
            addexpenses(cdict)
        elif menuofchoices == 2:
            vexpenses(cdict)
        elif menuofchoices == 3:
            vsummary(cdict)
        elif menuofchoices == 4:
            print("Goodbye!") # Goodbye message
            break
        else:
            print("Invalid option. Please choose 1–4.\n")

if __name__ == "__main__":
    main()