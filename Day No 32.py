# ---------------------- Day 32 -------------------
#                   Ramadan 10
#                   ------------------

# Sets Methods in python 

s1 = {1,2,3,4,5}
s2 = {2,3,5,6,7}

# Two sets are given perfrom some task on this sets

# 1. union()  and update()

# union()
print(s1.union(s2))

# update()

s1 = {1,2,3,4,5}
s2 = {2,3,5,6,7}
s1.update(s2)
print(s1,s2)

# 2. intersection() and update()

# intersection()
s1 = {1,2,3,4,5}
s2 = {2,3,5,6,7}
s3 = s1.intersection(s2)
print(s3)

# update()
s1.update(s2)
print(s1)


# we can also used with string datatypes such like this 
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities2 = {"Dankmark","spain","Berlin","Dehli"}

cities1.update(cities2)
print(cities1)

cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities2 = {"Dankmark","spain","Berlin","Dehli"}

print(cities1.union(cities2))
print(cities1.intersection(cities2))

# 3. symmetric_difference() in python
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities2 = {"Dankmark","spain","Berlin","Dehli"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)

# 4. difference() and difference_update()
print("difference() and difference_update()")
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities2 = {"Dankmark","spain","Berlin","Dehli"}
cities3 = cities1.difference(cities2)
print(cities3) 

# Sets Methods

# isdisjoint() method
# Two set are said to be disjoint if have have no in common
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities2 = {"Dankmark","spain"}
print(cities2.isdisjoint(cities1))

# issuperset() method
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities2 = {"Berlin","Dehli"}
cities3 = cities1.issuperset(cities2)
print(cities3) 

# issubset()Method
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities2 = {"Berlin","Dehli"}
cities3 = cities1.issuperset(cities2)
print(cities3) 

# add() Method 
cities2.add("spain")
print(cities2)

# update()
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities2 = {"Berlin","Dehli","spain","norway"}
print(cities1.update(cities2))

# remove() and discard()
#  ---> remove --> it will appears error raises
#  ---> discard --> but the discard not appears the error

# remove()
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities1.remove("Tokyo")
print(cities1)

# discard()
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities1.discard("Tokyo")
print(cities1)

# pop 
# --> catch the value , you can also access on your choose

# discard()
cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
cities1.pop()
print(cities1)

# cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
# cities1 = {"Tokyo","Madrid","Berlin","Dehli"}
# del cities1
# print(cities1)

# clear()
cities ={"Tokyo","Madrid","Berlin","Dehli"}
cities.clear()
print(cities  ) 


