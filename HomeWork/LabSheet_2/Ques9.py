# 9.Using a while loop, write a program that prints the Fibonacci
# series up to a given number.

a = 0
b = 1

print(a)
print(b)
n = int(input("Enter last term of fibonacci series : "))
for i in range(1,n+1):
    next = a + b
    a = b
    b = next
    
print(next)