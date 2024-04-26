# ---------------------- Day 12 -------------------
#                   Date  16-03-2024 
#                   -------------------
# **************** String Slicing *******************
# name slicing in python 
name = " shahbaz junaid "
names = "harry"
full_name = len(name)
print(name) # in this we print simple name 
print(len(name)) # in this line we print the length of string characters
print(name.lower())  
print(name.upper()) 

# There are two types of ' string slicing '
'''
   
i. positive (+ve ) slicing       
ii. negative (-ve ) slicing
  
'''
print( " This is -ve Slicing \n") 
print(name[:])  
print(name[7])  # This is print one character
print(name[0:7])  # this is print 0 to 6

print( " This is -ve Slicing \n")
print(name[3:-7])      
print(name[:-6])    
print(names[-4:-2])         
  
Name = "shabi"
print(len(Name))

mn = "harry"
print(mn[-4:-2])

print("simple for loop")
alphabats = "ABCD"
for i in alphabats:
    print(i)
    
Name = "shahbaz junaid shabi"
for c in Name:
    print(c)    