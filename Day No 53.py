# ---------------------- Day 53 -------------------
#                  Ramadan 16

"""
    map()
    filter()
    reduce()
    
    """
    # Map 
    
def cube(x):
    return x*x*x

print(2)    

l = [1,2,3,4,5,6,2,1]

newl = list(map(cube,l))
print(newl)


# filer

def filter_function(a):
    return a > 2

newl2 = list(filter(filter_function,l))
print(newl2)


newl3 = list(filter(lambda x : x*x*x,l))
print(newl3)


# reduce 

from functools import reduce 

l = [1,2,3,4,5,6,2,1]

def sum(x,y):
    return x+y

sum = reduce(sum,l)
print(sum)