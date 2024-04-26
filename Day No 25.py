# ---------------------- Day 25 -------------------
#                     Ramadan 8

#                   ------------------

#  ***************** Tuple() Methods ***************
'''
Tuple are immutable . Hence if you want to add , remove or change tuple item 
then the first you must convert the tuple to a list .
Then perform operation on that list and convert it back to tuple.

'''

countrie = ("spain","italy","india","england","germany")
temp = list(countrie)
temp.append("russian")  #add 
temp.pop(3) #remove
temp[2]="finland"
countrie = tuple(temp)
print(countrie)


# Note : Tuple convert list convert Tuple
#Concatenation two tuple
countrie1 = ("spain","italy","india","england","germany")
countrie2= ("spain","italy","india","england","pakistan")
concat = countrie1 + countrie2
print(concat)



#  Tuple Methods 

'''
-->count
-->index(element,start,end)
-->len(variable)

'''
# -->count

tup = (1,2,3,4,5,6,5,6,5,5,)
print(tup.count(5))

# -->index(element,start,end)

# for simple index

tup = (1,2,3,4,5,6,5,6,5,5,)
print(tup.index(5))


# index(element,start,end)
tup = (1,2,3,4,5,6,5,6,5,5,)
print(len(tup))
print(tup.index(5,0,10))




