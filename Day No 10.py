# ---------------------- Day 10 -------------------
#                   Date  15-03-2024 

#                   -------------------
# ********************* User - input ************
#  We are give to the user input() by the variables
#                    Exmale: a = input()
#                            a = input(" aslo used string b/w the braces")

#                            a = int(input(" what is favorite Number "))
#                     variable = datatype(input("string texts"))
#        This is an example of user input()  

print(" hi ! This is shahbaz junaid ")  
a = input("Enter your first Number \n ")  #\n  use for next line 
b = input("Enter your second Number \n ") 
print(a + b ) # This is print exits b/c the flow concatenation a and b # this is not into integer 
Name = "shahbaz"
print("My name is "+ Name)
print("The Arithmetic Operation ")
print( int(a) + int (b)) #We are using the type casting and this is explicit type casting
print(int(a)- int(b)) 
print(int(a)* int(b)) 
print(int(a)/ int(b)) 
print(int(a)** int(b)) 

# This is a Simple Calculator using the user input()
  
print("This is Simple Calculator to perfrom Simple tasks")
a = int(input("Enter your first Number \n "))  #\n  use for next line 
b = int(input("Enter your second Number \n "))   
print("All Arithmetic Operator ") 
print(" Addtion ",(a+b)) 
print(" subtracting ",(a-b))
print(" multiplication ",(a*b))     
print(" division",(a/b))      
print(" Modulus' reminder ' ",(a%b))      
print(" Floor Division(It can give point/decimal value) ",(a//b))  
print("  \' exponential operation  \'" ,(a**b)) # actualy power    