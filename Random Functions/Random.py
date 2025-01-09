import random

print(random.random()) # Returns a random float between 0.0 and 1.0
print(random.randint(1, 10))  # Returns a random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))# Returns a random fruit from the list
print(random.uniform(1,10)) # Returns a random floating-point number between 1 to 10

# Shuffling a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list) 


population = ['red', 'blue', 'green', 'yellow']
print(random.choices(population,k=3)) 

population = list(range(10)) 
population = [0,1,2,3,4,5,6,7,8,9]
print(random.sample(population, 5)) 


random.seed(a=8)
print(random.random()) # Returns the same random float every time this code runs, e.g., 0.57140259469
