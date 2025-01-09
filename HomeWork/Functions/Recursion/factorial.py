def fact(n):
    if(n == 0 or n == 1): return 1
    result = n * fact(n - 1)
    return result
    
x = int(input("Enter a number: "))
 
print(fact(x))
    