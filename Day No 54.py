# ---------------------- Day 54 -------------------
#                  Ramadan 16


# "is" vs "==" in python

# is for use identity 
# == comparision operators  
a = 3
b = 3

print(a is b )
print(a == b )

# list[]
l = [1,2,3]
m = [1,2,3]
print(type(l))
# is false because list is changable they different memory location
print(l is m)
print(l == m)


# sets{}
sets = {1,2,3}
sets1 = {1,2,3}

print(type(sets))
print(sets is sets1)
print(sets == sets1)

# tuples ()
tup = (1,2,3)
tup1 = (1,2,3)
print(type(tup))
print(tup is tup1)
print(tup == tup1)


# dictionary {key value pair }
dic = {"Name" :"shahbaz Juanid"}
dic1 = {"Name" :"shahbaz Juanid"}

print(type(dic))
print(dic is dic1)
print(dic == dic1)

a = None
b = None
print(a is None)
print(a is b)
print(a == b)