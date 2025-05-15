
print("Welcome to the Inventory Manager!")

# Display the inventory
print("\nCurrent Inventory:")
inventory = { "apple": (10, 2.5), "banana": (20, 1.2)} 
for item in inventory:
    quantity, price = inventory[item] # the values inserted for each item
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price}") # prints out each item with quantity and price

# Option to Add item
addanything = input("\nDo you want to add anything? Y/N ").strip().upper() # makes it lowercase y to upper case 
if addanything == 'Y':
    # makes user add parameters for an item
    addinput = input("Add a new item: ")
    addquantity = int(input("Enter quantity: "))
    addprice = float(input("Enter price: "))
    inventory[addinput] = (addquantity, addprice)
    print(f"Added '{addinput}' to inventory.")

# Option to Remove item
removeanything = input("\nDo you want to remove anything? Y/N ").strip().upper() # makes it lowercase y to upper case 
if removeanything == 'Y':
    removeinput = input("Remove an item: ")
    if removeinput in inventory:
        del inventory[removeinput] # if item is in the inventory, its gone
        print(f"Removed item: {removeinput}")
    else:
        print(f"Item '{removeinput}' not found.") # Error if the item is not in the inventory

# Option to Update item
updateanything = input("\nDo you want to update anything? Y/N ").strip().upper() # makes it lowercase y to upper case 
if updateanything == 'Y':
    updateitem = input("Update an item: ")
    if updateitem in inventory:
        # Updates the item's parameters
        updatequantity = int(input("Update the item's quantity: "))
        updateprice = float(input("Update the item's price: "))
        inventory[updateitem] = (updatequantity, updateprice)
        print(f"Updated {updateitem} — Quantity: {updatequantity}, Price: ${updateprice}")
    else:
        print(f"Item '{updateitem}' not found.") # Error if the item is not in the inventory

# Displays final updated inventory
print("\nUpdated Inventory:")
for item in inventory:
    quantity, price = inventory[item]
    print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

# Total value (Bonus)
totalvalue = 0
for item in inventory:
    quantity, price = inventory[item]
    totalvalue += quantity * price

print(f"\nTotal value of inventory: ${totalvalue:.2f}")
