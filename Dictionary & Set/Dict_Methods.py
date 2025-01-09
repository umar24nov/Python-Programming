info = {
    "Name" : "Mohd Umar",
    "Age" : 21,
    "is_adult" : True,
    "Subjects" : ["Python","Java"],
    "Topics" : ("dict","sets")
}



# print(info.keys()) # Return all the keys
# print(info.values()) # Return all the values
# print(info.items()) # Return all the key value pairs
# pairs = list(info.items()) 
# print(pairs[0]) # Return 0th index pair
# print(len(info))
# print(len(list(info.keys())))

# print(info["Name"])
# print(info.get("Name")) #Both returns same

# print(info["Name2"]) #Error
# print(info.get("Name2")) #No Error
info.update({"City" : "Delhi"})

print(info) # This will print updated dictionary
