# Fibonacci Series : 1,1,2,3,5,8,13,21,34...
def fibo(n):
    if (n == 1 or n == 2): return 1
    result = fibo(n - 1) + fibo( n - 2)
    return result
x = int(input("Enter a number : "))
print(fibo(x))