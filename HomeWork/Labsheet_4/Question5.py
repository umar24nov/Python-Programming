

def prod_and_sum(*args):
    total_sum = sum(args)
    product = 1
    for num in args:
        if num != 0:
            product *= num
    return total_sum, product

# Example usage:
numbers = [3, 5, 0, 2, 1]
sum_result, product_result = prod_and_sum(*numbers)

print(f"Sum of numbers: {sum_result}")
print(f"Product of non-zero numbers: {product_result}")
