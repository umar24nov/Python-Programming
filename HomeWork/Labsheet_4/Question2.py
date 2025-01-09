def sum_of_digits(num):
    if (num == 0):
        return 0
    else:
        return (num % 10) + sum_of_digits(num // 10)

x = int(input("Enter a 5-digit number: "))
print(sum_of_digits(x))
