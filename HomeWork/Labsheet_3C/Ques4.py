# 4. From question 3.d, access the elements of sets, multiply them by a 
# variable whose value is updating from 1 to N for respective element 
# of the set, and then print them with space separation.
# For example, set is {1,4,6, 1, 5}, the output should be :
# 1 8 18 4 25
# Explanation: Output is 1x1 = 1, 4x2 = 8, 6x3 = 18, 1x 4 = 4 and 5x5=25.


# Define the set
my_set = {1,3,5,7,9}

# Convert the set to a list to maintain order
my_list = list(my_set)

# Loop through the elements with index starting from 1
for i in range(1, len(my_list) + 1):
    # Multiply element by its respective index
    result = my_list[i - 1] * i
    print(result, end=" ")
