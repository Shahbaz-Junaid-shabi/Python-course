# #  ------------ Day N0:21 ---
# #               Ramadan 5

# # Function Arguments  
# def average(a,b):
#     print("the Average is ", (a+b)/2)
    
# average(4,6)    
# # Default arguments 
# def averagae(a=10,b=10):#It ignore the Default Arguments 
#     print("the Average is ", (a+b)/2)
    
# average(4,6) #and here this will execute

# # 
# def name(first,last = "junaid"):
#     print("hi",first,last)
    
# name('shahbaz')

# # keyword Arguments
# # we also change the order of argument in function 
# # we don't care the of argument in function
# def name(first,second,third):
#     print("Hello",first,second,third)

# name(second="junaid",first="shabi",third="shabi") 

# def fullname(first,last):
#     print("Hi",first,last)
#     print("Good Morning!")
# c = fullname(last=" Juanid",first="Shahbaz")
# print(c)
# print(type(c))
# # In keywords arguments we don't care the argument pass unorderly 

# # Required Argument 

# # In case the don't pass the argument withea key=value syntax
# # then it is necessary to pass the argument in the correct position order.

# # it is necessary to give the Required argument 
    
   
# # Required arguments 
# def averagae(a,b=10):#It ignore the Arguments 
#     print("the Average is ", (a+b)/2)
    
# averagae(10)  

# # Variable-Length Arguments

# def name(*name):
#     print(type(name))
#     print("Hellow",name[0],name[1],name[2])

# name("shahbaz","Junaid","Shabi")    
# #
# # Anthor exmaple 
# # As a Tuples
# def AMean(*numbers):
#     sum = 0 
#     for i in numbers:
#      sum = sum + i 
#     print('The AMean of Number is = ',sum/len(numbers))
    
# AMean(3,4,4,56)

# # As Dictionary 


# def name(**name):
#     print(type(name))
#     print("Hellow",name["fname"],name["mname"],name["lname"])

# name(fname="shahbaz",mname="Junaid",lname="Shabi")
# # key value pair 


# def fullname(first,last):
#    return (first,last)

# c = fullname(last=" Juanid",first="Shahbaz")
# print(c)
#   ------------ Day N0:21 ---
#               Ramadan 6

# --------- list --------- 
# list of 30 day challenge
# list of marks of students of class 10th
# list of people enrolleed in hundreds day of code
# we make list for easy to understandable 

# listone = ["shahbaz","junaid","shabi"]
# print(listone)
# print(listone[0])
# print(listone[1])
# print(listone[2])

# l = [1,5,7]
# print(l)
# print(l[0])
# print(l[1])
# print(l[2])

# print(l[:])
# # Negative Indexing 
# print("\n Negative Indexing \n")
# print(l[-1])
# print(l[-2])
# print(l[-3])

# if 5 in l:
#     print("Yes")
# else:
#     print("No")    
    
# if "shabi" in listone:
#     print("Yes")    
# else:
#     print("No")
    
#     # List comprehension 
# lst = [i for i in range(10)]    
# print(lst)  
# lst = [i*i for i in range(10)]    
# print(lst)  
# lst = [i*i for i in range(10)if i%2==0]    
# print(lst)  

    
# #               Ramadan 7


# #                   ------------------

# #  ***************** list [] Methods ***************

# # List Methods of the list are follow :
# '''
# i) append(value)
# ii) sort(variable)
#   -->sort(reverse=True)
# iii) reverse()
# iv) index(index)
# v) count(value)
# vi) copy()
# vii) insert(index,value)
# vii) extend(value)
# '''
# list_01 = [1,7,5,4]
# print(type(list_01))
# print(list_01)

# # i) append(value)
# # Add the vaule in list
 
# list_01.append(12)
# print(list_01)

# # ii) sort(variable)
# #  This method sort the list in ascending order 

# list_01.sort()  
# print(list_01)    
# #   -->sort(reverse=True)

# list_01.sort(reverse=True)   #It print the value in descending order
# print(list_01)  

# # iii) reverse()

# list_01.reverse()
# print(list_01)

# # iv) index(index)
# #              The method returns the index if the first occurance of the list item.
# print('indexing')  
# list_02 = [1,2,4,5,6,2]  
# print(list_02.index(1))

# # v) count(value)
# # Returns the count of the numbers of item with the given value 
# print(list_02.count(4))

# # vi) copy()

# newlist = list_02.copy()
# print(newlist)

# # vii) insert(index,value)
# #             if you want insert value then 

# m = [900,1000,1100]
# m.insert(0,800)
# print(m)

# # vii) extend(value)
# # Add an entire list or any other collection dtattype

# list_02.extend(m)
# print(list_02)


# list1 = [1,2,3,4]
# list2 = [5,6,7]
# print("simple concatenation")
# k = list1 + list2
# print(k)


#               Ramadan 8

# # Tuples()
# tuples =(1)
# print(tuples)
# print(type(tuples))

# print("Single Tuple ")
# tup = (1,) #comma is necessary if you want to make 1 or single tuples
# print(tup)
# print(type(tup))

# tup = (10,20,30,40)
# print(tup)
# # Tuples is unchangeable

#               Ramadan 8

# Tuple is immuteable 

# countrie = ("spain","italy","india","england","germany")
# temp = list(countrie)  # convert into list
# temp.append("Pakistan") #add
# temp.pop(2)  #remove 
# temp[2] = "Afgani"   #change 
# countrie = tuple(temp)  # convert into tuple 
# print(countrie)

# #               Ramadan 8
# # doc string 
# def sqare(n):
#     "Taking sqare of any Number is "
#     print( n*n)
# sqare(10)
# print(sqare.__doc__)
# print(type(sqare.__doc__))

#         Ramadan 10

# union()

sets1 = {1,2,3,4,5,6,}
sets2 = {1,3,5,6,8,9,10}
print("union",sets1.union(sets2))

# print(sets1.union(sets2))

# update for any one sets1 or sete2

sets1.update(sets2)
print("Use the update Method ",sets1)

# also exists use the intersection 

# intersection
sets1 = {1,2,3,4,5,6,}
sets2 = {1,3,5,6,8,9,10}
print("intersection",sets1.intersection(sets2))

# print(sets1.union(sets2))

# update for any one sets1 or sete2

sets1.intersection_update(sets2)
print("Use the update Method ",sets1)



sets1 = {1,2,3,4,5,6,}
sets2 = {1,3,5,6,8,9,10}
print(sets1.symmetric_difference(sets2))
# Not common value 

# Methods of sets 

sets1.difference
sets1.difference_update
sets1.isdisjoint #one common in sets
sets1.issuperset #common in sets
sets1.issubset

# add

# if you want add the element in sets then us add.
sets1 = {1,2,3,4,5,6,}
sets1.add(999)
print(sets1)














