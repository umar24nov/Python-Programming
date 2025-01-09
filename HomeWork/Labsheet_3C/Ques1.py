# A set contains names which begin either with A or
# with M write a program to separate out the names into
# two sets, one containing names beginning with A and 
# another containing names beginning with B.

names = {"Amir", "Aajam", "Mohd Sahib", "Abdullah", "Mohd Umar", "Mohd Ayaan"}

a_names = set()
b_names = set()

names_list = list(names)

for i in range(len(names_list)):
    if names_list[i].startswith('A'):
        a_names.add(names_list[i])
    elif names_list[i].startswith('M'):
        b_names.add(names_list[i])
        
print(a_names)
print(b_names)

