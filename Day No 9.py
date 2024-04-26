# ---------------------- Day 9 -------------------
#                   Date  15-03-2024 
 
#                   -------------------
# *********************** TypeCasting *****************

# pervious lecture Work 
a = 10
b = 20 
print( " The value of ",a," + " ,b, " = ",(a+b) )   
print( " The value of ",a," - " ,b, " = ",(a-b) )    
print( " The value of ",a," * " ,b, " = ",(a*b) )   
print( " The value of ",a," / " ,b, " = ",(a/b) )   
print( " The value of ",a," // " ,b, " = ",(a//b) )   

# TypeCasting : 
#              The Conversion / convert one datatype into other datatype
#              Example : a = " 1 "
#                        b = " 2 "
#                        print(a+b)
#  Python support a wide varity of methods like : int(), float(), str(),ord(),hex()
#                                                  oct(),tuple(),set(),list(),dict() etc.

# There are two types of typecasting :
# i) Explicit typecasting---> Example :
#                             a = "1"
#                             b = "2"
#                             print(int(a)+int(b))
#                     The data is typecasting by the programmer string() convert into int()

# ii) Implicit  typecasting---> Example :
#                              a = 1.1
#                              b = 1 
#                              print(a+b)
#                     The do own Convert the datatype int() into float()

print(" This is an example of Explicit typecasting str() convert into int()\n")
a = "1" 
b = "2"
print(int(a)+int(b)) 
print(" This is an example of ixplicit typecasting int() convert into float()\n")
# The python compiler convert automatically 
a = 1
b = 1.2
print((a+b))  
print(type(a+b)) 