import math
def square(a):
    area =  a ** 2
    perimeter = 4 * a
    return area,perimeter
    
    

def circle(r):
    area =  3.14 * (r ** 2)
    perimeter = 2 * 3.14 * r
    return area, perimeter

def rectangle(l,b):
    area =  l * b
    perimeter = 2 * (l + b)
    return area, perimeter

print(square(5))
print(circle(5))
print(rectangle(3,4))