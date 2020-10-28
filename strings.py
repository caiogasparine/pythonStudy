# using text. functions - specific for strings
text ="Python Code Test - String Manipulation"
print(text.upper())
print(text.find('o'))     # will return the index of the letter o in var text
print(text.replace('a','4'))

print('Test' in text)     # return true or false

# math operators
print('Math Operators Results:')
print(10/2)               # return the division result
print(10//2)              # return only the integer value
print(10%2)               # return the reminder
print(10**2)              # return 10^2

x = 10 + 3 * 2            # operator precedent - first */ and then +/-
                          # parentheses can change it

# boolean values          == equality operator != not equal >,>=,<,<=
print(4<7)

# logical operators       OR AND NOT
age = 25
print(age > 10 and age < 26)
