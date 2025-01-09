my_set = {1,5,8,3,2}

# Convert the set to a list to maintain order
my_list = list(my_set)

results = []
# Loop through the elements with index starting from 1
for i in range(1, len(my_list) + 1):
    # Multiply element by its respective index
    result = my_list[i - 1] * i
    print(result, end=" ")
    results.append(result)
# Caluclating sum of elements in result 
sum = 0
for j in range(len(results)):
    sum += results[j]
    
min_result = min(results)
max_result = max(results)

print("\n")


print("Sum:", sum)
print("Min:", min_result)
print("Max:", max_result)

sorted_results = sorted(results)

for ele in sorted_results:
    print(ele, end=" ")
    
