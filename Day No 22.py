# ---------------------- Day 22 -------------------
#                   Ramadan 7
#                   ------------------

#  ***************** list [] ***************
list = [10,32,34]
print(list)
print(type(list))

print(list[0])
print(list[1])
print(list[2])

'''

--> one variable store Multiple data such as student: marks,odd number and family etc.
--> Lists are called collection of data items
--> They store multiple items in a single variable
--> List items are separated by commas and enlcose within square bracket[]
--> List are changable meaning we came alter than after creation 
-->  list are store d/f datatypes like the string and boolean and other dataypes
--> In list multiple or differnt datatype in involved or comtain
--> In list indexing start with 0 .
'''

color = ["red","yellow","blue",'green']
print(type(color))
print(color)

# Negative indexing in list in python
value = [10,12,23,45]
print(value)
# print(value[0:len(value)])  list starting with 0 and ending with len(of variable)

print(value[-3]) #convter into positive index
print(value[1])

# check weather an items in present in the list

if 10 in value :
    print("Yes it is persent")
else:
    print("No it is not persent")    

# also used with string datatype

# JAMPING INDEXING 

# ListName[start,end,Jump]

numbers = [12,223,4,34,545,545,45,65,23,34,10]

print(numbers)
print(numbers[1:10:2])
# 2 is us jumping index 

# List Comprehensive 
'''                are used for creating new list from iterables like lists,tuple 
 dict,set and even in array and string 
 
 syntax : list = [Expression(item) for item in ifcondtion]
    print(list)     
                   
'''


    # List comprehension 
lst = [i for i in range(10)]    
print(lst)  
lst = [i*i for i in range(10)]    
print(lst)  
lst = [i*i for i in range(10)if i%2==0]    
print(lst) 
list_01 = [i for  i in range(10)]
print(list_01)

list_01 = [i*i for  i in range(10)]    #any operation can you gives 
print(list_01)



