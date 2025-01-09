# 3. create two sets: a= {10, 25, 4, 12, 3, 8} and 
# b = {4, 13, 3, 12, 9, 17, 25}. Find the following and store 
# in different variables:
# a. union of sets
# b. intersection of sets
# c. difference; the elements present in a but not in b as well
# as the elements present in b but not in a
# d. symmetric difference
# e. intersection between the results of b and d
# f. union of the results of b and d
# g. compare the results of a and f

a = {10, 25, 4, 12, 3, 8}
b = {4, 13, 3, 12, 9, 17, 25}

# union of sets
uni = a.union(b)  # a
print(uni)

# intersection of sets
intr = a.intersection(b)  # b
print(intr)

# difference
diff = a.difference(b)  # c
print(diff)

# symmetric difference
sym_diff = a.symmetric_difference(b) # d
print(sym_diff)

# intersection between the results of b and d
intr_b_d = intr.intersection(sym_diff) # e
print(intr_b_d)

# union of the results of b and d
uni_b_d =  intr.union(sym_diff)  # f
print(uni_b_d)

# Comparing results of a and f

print(uni == uni_b_d)
