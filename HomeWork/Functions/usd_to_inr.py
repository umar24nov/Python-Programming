# Function to convert USD to INR
# 1 USD = 84 INR

def usd_to_inr(number):
    number = number * 84.03
    return number

x = float(input("Enter a number : "))

print(usd_to_inr(x))