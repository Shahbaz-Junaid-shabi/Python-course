# ---------------------- Day 21 -------------------
#                   Date  01 - 12 -2023 
#                   ------------------

#  *****************  Function() Arguments  ***************
# Function is used for sperate code 
def average(a,b):
    print("The average of a and b is ",(a+b)/2)
    
average(10,20)    #we can also used semicolon
average(20,40);   #again funtion call

"""
    There are four types of Function Argument 
    i) Default Arguments
    ii) Keywords Arguments
    iii) Variable length Arguments
    iv)  Required Arguments
    

    """
# i) Default Arguments

def average(a,b):
    print("The average of a and b is ",(a+b)/2)
    
average(10,20)    #we can also used semicolon
average(20,40);

#   OR
def average(a=40,b=20): #this is default values
    print("The average of a and b is ",(a+b)/2)
    
average();    #we can also used semicolon
average(a=20);    
average(b=60);   

# we can also change its value such a = value , and  b = value 

# For string data

def stringdata(Name,MiddleName,lastName):
    print("Hi! My name is ",Name,MiddleName,lastName)

stringdata("shahbaz","Junaid","S/o Ghulam Rasool")    
    
    # DIFFERENT B/E Formal and Actual Arguments 
#  Formal Argument ----> such as variable a , b and Num1 ,Num2 etc 
   
#  Actaual Argument ----> such as value in integer from and also another datatype in program language     
 
#  ii) Keyword Arguments 
   
def stringdata(Name,MiddleName,lastName):
    print("Hi! My name is ",Name,MiddleName,lastName)

stringdata(MiddleName="Junaid",Name="Shahbaz",lastName="S/o Ghulam Rasool") 

# Note : The order in which the argument are pass does not matter
# Note : Order is doesn't matter 

# For value 
def average(a,b):
    print("The average of a and b is ",(a+b)/2)
    
average(b=50,a=20)

# iii) Required Arguments 
"""
It id necessary to pass the arguments in the correct positional order
and number of argument pass should match with actual function definition.
"""
def average(a,b):
    print("The average of a and b is ",(a+b)/2)
    
average(10,20)
# average(10) # b is missing then the compiler throws the Missing Arguments error

# iv) Variable Length Arguments

"""
 Sometime we may need to pass more argument than those defined in the actual than those defined in the actual function . This can be done using variable 
 length argument 
  
"""

def average(*value):   # one *value is used for tuple()
    # print(type(value))
    sum = 0
    for i in value:
     sum = sum + i
    print("The average of mutiple NO :", sum/len(value))

average(5,5,10,14,12)   

def name(**name):   # one **name is used for dictionary()
    # print(type(name))
    print("My name is ",name["FName"],name["LName"])

name(FName = "shahbaz",LName ="junaid")    