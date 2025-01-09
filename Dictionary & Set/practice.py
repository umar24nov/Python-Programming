# WAP to enter marks of three subjects from the user and store 
# in  a dictionary. Start with an empty dictionary and add one by one.

marks = {}
x  = int(input("Enter Physics marks : "))
marks.update({"Physics" : x})

x  = int(input("Enter Chemistry marks : "))
marks.update({"Chemistry" : x})

x  = int(input("Enter Maths marks : "))
marks.update({"Maths" : x})

print(marks)
