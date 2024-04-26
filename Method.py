# List Methods of the list are follow :
'''

i) append(value)
ii) sort(variable)
  -->sort(reverse=True)
iii) reverse()
iv) index(index)
v) count(value)
vi) copy()
vii) insert(index,value)
vii) extend(value)

'''  
# ----- This are also the Array Methods Visualised
# push
# unshift
# pop
# shift
# filter
# map((0)>=0)
# join("-")
# concat
# flat
# slice(1,3)

# list Methods 

# -------  append()------
# append() is use for adding value or data in list
print("----------append()--------")
 
l = [1,3,4,5]
print(l)
l.append(8)
print(l) #print After append(Your Data)

# -------  sort()------
# In sort() it arranged the value in Ascending Order.

print("----------sort()--------")
l = [2,4,9,5,7,1,8,10,3,6]
l.sort()
print(l)

# -------  sort(reverse = True)------
# In sort() it arranged the value in Ascending Order.

print("----------sort(reverse=True)--------")
l = [2,4,9,5,7,1,8,10,3,6]
l.sort(reverse=True)
print(l)

# -------  reverse()------
# It reverse the list 
print("----------reverse()--------")

l = [2,4,9,5,7,1,8,10,3,6]
print("before",l)
l.reverse()
print("After",l)

# -------  index() ------

print("----------index--------")
# give the index of the value where is it 
l = [10,20,30,40]
print(l)
print(l.index(30))

# -------  Count() ------
print("----------count--------")
# It count the value such most repeated value 
l = [10,20,30,40,10,50,10]
print(l)
print(l.count(10))

# -------  Copy() ------

print("-------Do not copy like this ------")
l = [10,20,30,40,10,50,10]
print(l)
m = l
m[0]= 0 
print(l)


print("----------copy--------")
# It copy of a list  
l = [10,20,30,40,10,50,10]
print(l)
print(l.copy())
# Or
l.copy()
print(l)


print("----------insert() --------")
# Add values are also called insert

l = [10,20,30,40,50]
print(l)
l.insert(0,0)
l.insert(6,60)
print(l)

print("----------extend() --------")

l = [10,20,30,40,10,50,10]
m = [1,2,3,4,5]
print(l)
print(m)
l.extend(m)
print(l)

# another method 
print("Another method to extend list in python ")
l = [10,20,30,40,10,50,10]
m = [1,2,3,4,5]

n = l+m
print(n)




