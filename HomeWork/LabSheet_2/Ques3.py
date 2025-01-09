# 3. Write a Python program using logical operators to checkif a number
# lies between two other numbers. Take all three numbers in the input 
# and check the above for the third input.

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
num3 = float(input("Enter third number : "))

if(num1 < num3 < num2) or (num2 < num3 < num1):
    print(f"The number {num3} lies between {num1} and {num2} .")
else:
    print(f"The number {num3} does not lies between {num1} and {num2} .")