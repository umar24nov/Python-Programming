# Check if an element exists in the resulting tuple of question 2.

tuple1 = (10, "Hello", 3.14, True)
tuple2 = ('a', 15.6, False, ["Umar",5.6,None])

concatenated_tuple = tuple1 + tuple2
repeated_tuple = concatenated_tuple * 2

element_to_check = 25

exists = element_to_check in repeated_tuple

if(exists != 0):
    print("Exists.")
else:
    print("Does not exists.")