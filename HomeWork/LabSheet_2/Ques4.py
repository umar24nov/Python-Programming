# 4. Write a Python program using if-else to find the largest
# of three numbers.

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
num3 = float(input("Enter third number : "))

if(num1 >= num3 and num1 >= num2):
    print(f"{num1} is greatest among three.")
elif(num2 >= num3 and num2 >= num1):
    print(f"{num2} is greatest among three.")
else:
    print(f"{num3} is greatest among three.")