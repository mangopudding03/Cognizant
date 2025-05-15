# Task 1

print("\n Task 1")

fruits = ['Apple', 'Mango' , 'Lychee' , 'Banana' , 'Papaya'] #List of my favorite fruits 
print("Original list: ", fruits)
# append

fruits.append('Strawberry')
print("After adding a fruit: ",fruits)

# remove

fruits.remove('Strawberry')
print("After removing a fruit: ",fruits)

# reverse
print("Reversed list: ",fruits[::-1])

# Task 2

print("\n Task 2")

whoami = {"name": "Maanya", "age": 22, "city": "Cincinnati"} #myinfo

print("Original dictionary: ", whoami)

# add new key for favorite color
whoami["favorite color"] = "mint green"

print("After adding favorite color key: ",whoami)
# update city with new value
whoami["city"] = "Mason"
print("New city: ", whoami)

# Print Keys
print("Keys:", end=" ")
keycount = 0
totalkeys = len(whoami.keys())
for key in whoami.keys():
    keycount += 1
    if keycount < totalkeys:
        print(key, end=", ")
    else:
        print(key)  # doesn't comma the end

# Print Values
print("Values:", end=" ")
valuecount = 0
totalvalues = len(whoami.values())
for value in whoami.values():
    valuecount += 1
    if valuecount < totalvalues:
        print(value, end=", ")
    else:
        print(value)  # doesn't comma the end


#Task 3

print("\n Task 3")
fav = ('Final Destination', 'Cry For Me', 'Verity') #My favorite things
print("My favorite things: ", fav)

try:
    fav[0] = 'Insidious' # Changing my fabv movie
except TypeError:
        print("Oops! Tuples cannot be changed.") #Error because tuples cannot be changed

print("Length of tuple:", len(fav))