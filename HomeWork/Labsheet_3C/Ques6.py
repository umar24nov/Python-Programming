# 6. Create a list of cricketers with different names. Use this
# list to create a dictionary in which the list values become keys
# of the dictionary. Set the values of all keys to 50 in the dictionary created.

my_list = ["Virat Kohli", "Rohit Sharma", "Jasprit Bumrah"]

my_dict = {name : 50 for name in my_list}

print(my_dict)
