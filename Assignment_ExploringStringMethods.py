
print("Task 1")
textstring = "Python is amazing"
#First word
print("First word: ",textstring[:6])
#Amazing part
print("Amazing part: ", textstring[10:17])
#Reversed string
print("Reversed string: ",textstring[::-1])

print("\n Task 2")
textstring2 = " hello, python world! "

textstring2stripped = textstring2.strip()                  # Remove leading/trailing spaces
capitalized = textstring2stripped.capitalize()         # Capitalize first character
replaced = textstring2stripped.replace("world", "universe")  # Replace word
uppercased = textstring2stripped.upper()               # Convert to uppercase

print("textstring2stripped:", textstring2stripped)
print("Capitalized:", capitalized)
print("Replaced 'world' with 'universe':", replaced)
print("Uppercase:", uppercased)

print("\n Task 3")
word = input("Enter a word: ").strip()
if word.lower() == word[::-1].lower():
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"Nope, '{word}' is not a palindrome!")
