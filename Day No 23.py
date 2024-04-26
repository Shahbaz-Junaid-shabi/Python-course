# ---------------------- Day 23 -------------------
#                   Ramadan 8

#                   ------------------

#  ***************** list [] Methods ***************

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
list_01 = [1,7,5,4]
print(type(list_01))
print(list_01)

# i) append(value)
# Add the vaule in list
 
list_01.append(12)
print(list_01)

# ii) sort(variable)
#  This method sort the list in ascending order 

list_01.sort()  
print(list_01)    
#   -->sort(reverse=True)

list_01.sort(reverse=True)   #It print the value in descending order
print(list_01)  

# iii) reverse()

list_01.reverse()
print(list_01)

# iv) index(index)
#              The method returns the index if the first occurance of the list item.
print('indexing')  
list_02 = [1,2,4,5,6,2]  
print(list_02.index(1))

# v) count(value)
# Returns the count of the numbers of item with the given value 
print(list_02.count(4))

# vi) copy()

newlist = list_02.copy()
print(newlist)

# vii) insert(index,value)
#             if you want insert value then 

m = [900,1000,1100]
m.insert(0,800)
print(m)

# vii) extend(value)
# Add an entire list or any other collection dtattype

list_02.extend(m)
print(list_02)


list1 = [1,2,3,4]
list2 = [5,6,7]
print("simple concatenation")
k = list1 + list2
print(k)



