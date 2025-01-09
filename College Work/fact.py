# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n - 1)

# n = 5

# print(f"Factorial of {n} is {fact(n)}")



# def fact(n):
#     if n == 0 or n == 1:
#         return 1
    
#     else: 
#         fac = 1
#         for i in range(1, n+1):
#             fac *= i
#         return fac

# print(fact(5))

import math

num = int(input("Enter a number : "))
print(f"Factorial of {num} is {math.factorial(num)}")