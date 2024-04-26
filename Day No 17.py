# ---------------------- Day 17 -------------------
#                   Date  18-03-2024 
 
#                   -------------------
#  *****************  Loop in python ***************
'''
i) For loop 
ii) while loop
it is called the iteration or loop 
'''
# We use firstly the for loop
# for print a Name 

name = "shahbaz"
for i in name:
    print(i)
    if i == "z":
     print("z is the last character ")
     
list_01 = ["red","yellow","blue","pink"]
for list_01 in list_01: 
    print(list_01)
    for i in list_01:
        print(i)     
    
# for print character     
name = "shahbaz"
for character in name:
    print(character)
    
print("----------------------------------------------------------------")
lists = ["apple", "banana", "cherry"]
for list in lists:
    print(list)
    
print("USING THE INDEXING AND PRINT THE VALUE OR STRING")    
lists = ["apple", "banana", "cherry"]
for index in lists:
    print(index) 
for k in range(10):
 print(k)
# for i in range(start,end,increament):
#  print(i)
# using the start,end and increament
print("print the increament by 2")
for i in range(0,20,2):
    print(i)
    
for i in range(100) :
    print(i)   
    
# print table on your choose enter no and create a table using the for loop
table = int(input("Enter Your table No :"))
print("your table No is :",table)  
for i in range(11):
    print(i,"*",table,"=",i*table)    