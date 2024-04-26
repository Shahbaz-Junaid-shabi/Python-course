# ---------------------- Day 24 -------------------
#                   Ramadan 8

#                   ------------------

#  ***************** Tuple() ***************

# Tuple in python
"""
              -->  Tuple are ordered collection of data item.
              -->  They stored multiple items in a single variable.
              -->  Tuple items are separated by commas and encolose within round brackets 
             --> Tuples are unchangable meaning we ca not alter them after creation 
             --> Tuple cannot be change such as 
             tup[0]=90 in python  
              
"""

tup = (
    1,
    2,
    3,
    4,
)
print(tup)

# If we create one tuple it is cannot consider as a tuple it is integer

tup = 1
print(type(tup))

# If you want to create one value tuple then use commas after value

tup = (1,)
print(type(tup))

# Note : +ve and -ve indexing also same with list[]
# and Slicing also same


# Tuples is unchangable 
tup = (10,20,30,40)
print(tup) 
print(len(tup))
print(tup[0]) 
print(tup[1]) 
print(tup[2]) 

# tup[2] = 999
# # Tuples is unchangable 
# print(tup) 

# Also enter another datatypes such as bool,int and string etc

# Also Slicing with Tuples 

# tuple = (start,end,Jump)
tup = (10,20,30,40,50,60)
print(tup[1:5])

# jumping index in Tuples
tup = (0,10,20,30,40,50,60,70,80,90,100)
tupe = tup[1:5:1]
print(tupe)