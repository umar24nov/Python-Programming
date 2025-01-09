# 5.Write a Python program to categorize a given integer as positive,
# negative, or zero using an if-elif-else ladder.

num = int(input("Enter an integer : "))

if(num > 0):
    print(f"{num} is a positive integer.")
elif(num < 0):
     print(f"{num} is a negative integer.")
else:
     print("The number is zero.")