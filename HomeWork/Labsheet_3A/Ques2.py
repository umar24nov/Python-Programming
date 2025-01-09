# Write a Python script to create a list 
# of integers and print only the even numbers.

numbers = [1, 2, 5, 4, 11, 6, 12, 8, 9, 10,14,20]

print("Even numbres are : ")

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(numbers[i])


