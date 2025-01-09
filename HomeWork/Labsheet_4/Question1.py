def sum(x):
    if (x == 0): return 0
    result = x + sum(x - 1)
    return result


n = int(input("Enter a number : "))
print(sum(n))
