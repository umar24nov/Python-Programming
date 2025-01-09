def sum(num):
    if (num == 0):
        return 0
    result = num + sum(num-1)
    return result

print(sum(5))