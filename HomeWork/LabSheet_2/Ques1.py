# 1. Write a Python program to perform addition, subtraction,
# multiplication, and division of two numbers entered by the user.

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if(num2 != 0):
    division = num1 / num2
else:
    division = "undefined as denominator is zero!"
print("Results : ")

print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")


    




