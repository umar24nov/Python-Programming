# 6.Using nested if statements, write a Python program to check 
# if a number is both divisible by 5 and even.

num = int(input("Enter a number : "))

if(num % 5 == 0):
    if(num % 2 == 0):
        print(f"{num} is divisible by 5 and is even.")
    else:
        print(f"{num} is divisible by 5 and is not even.")
else:
    if(num % 2 == 0):
        print(f"{num} is not divisible by 5 but is even.")
    else:
        print(f"{num} is neither divisible by 5 nor even.") 
        
