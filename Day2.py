# Day - 2
# Strings, Lists, and Smarter Logic

name = input("Enter your name: - ")

print("First letter: ", name[0]) # This prints the first letter of the given name which is on index 0 hence name[0].
print("Last letter: ", name[-1]) # This prints the last letter of the given name which is on index -1 as we do not know how long the name is and all hence name[-1].
print("Length of name: ", len(name)) # This prints the length of the given name like how many characters does it have.

print("Your name in UPPERCASE: ", name.upper()) # This will simply print the given name in uppercase.
print("Does you name start with an "R"?: ", name.startswith("R")) # Gives a boolean value of weather or not your name starts with the mentioned letter.

print("Your name repeated 3 times: ", name * 3) # Will multiply your name 3 times and give as an output.


sentence = "Python is awesome"

print(sentence[0:6]) # Will print the letter from index 0 to index 6 (python)
print(sentence[:6]) # Will do the same as above. If left empty, python will take it as 0.
print(sentence[7:9])
print(sentence[-7:])

reversed_sentence = sentence[::-1] # Reverses any given string.
print(reversed_sentence)


fruits = ["apple", "banana", "cherry"] # Makes a list of anything when written in [] and separated by ,

print("First fruit: ", fruits[0])
print("All fruits: ", fruits)

fruits.append("dragonfruit") # Adds an item to the list
print("New fruit list: ", fruits)

fruits.remove("banana") # Removes an item from the list
print("After removing banana: ", fruits)

print("Sorted: ", sorted(fruits)) # Sorts the list


groceries = [] # Creates an empty list

for i in range(5):
    item = input(f"Enter item {i+1}: ") # Will take input until the range is in check.
    groceries.append(item)

print("Your Groceries list: ", groceries)


password = input("\n Enter your password: ") # \n helps you skip a line before asking the question.

length = len(password) >= 8

has_upper = any(c.isupper() for c in password) # Checks if an uppercase letter exist in the input.
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)

if length and has_upper and has_lower and has_digit: # and helps you add multiple conditions to one statement.
    print("\nYour password is Strong!")
else:
    print("\nYour password is weak!")