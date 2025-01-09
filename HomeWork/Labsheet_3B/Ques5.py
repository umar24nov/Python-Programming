# 5. Write a Python program to input a string, convert
# it to uppercase, lowercase, title cased, capital cased and 
# print the length.

string = str(input("Enter a string : "))

upperCase = string.upper()
lowerCase = string.lower()
titleCase = string.title()
capitalCase  = string.capitalize()
stringLen = len(string)

print(upperCase)
print(lowerCase)
print(titleCase)
print(capitalCase)
print(stringLen)