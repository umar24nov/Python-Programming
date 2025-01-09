def fact(number):
    for i in range(1,number):
        number *= i
    return number
    

x = int(input("Enter a number : "))

print(fact(x))
