# ---------------------- Day 20 -------------------
#                   Date  01 - 12 -2023 
#                   ------------------

#  *****************  Function() in python  ***************
"""
---> Task perfrom seperatedly 
---> Logic used Multiple time
---> Make once used for ever 
---> For the blogs of code make function

Types
-----
 i) Built-in function ---> e.g=> void (),min(),range(),len(),print(),
                           type(),list(),tuple(),dict() and max() etc.
 ii)User-defined function  ----> e.g => def Amean(a,b):
                                           Amean = a+b/2
                                           print(Amean) 

 synatax:def Variable(parameters)
             Variable = a+b(operation)
             print(Variable)
             
---> For function call: 
         sum(a,b) 
         Note : Always used in the end with semicolon ;            
             
             
Example:          def sum(a,b)
                  sum = a+b
                  print(sum)
                sum();  
"""
a = 10
b = 16
def sum(a,b): # this is write first funtion in python and always cares it indentation 
 sum = a+b
 print("The sum of a and b is :",sum) 
  
sum(a,b) #function call look like this 

def Amean(a,b):
    Amean = a+b/2
    print("The Arithmetic mean of a and b is :",Amean)

Amean(a,b);    #at the end of function call use semicolon in python


c = int(input("Enter Your c value "))    
d = int(input("Enter Your d value "))    
def Amean(c,d):
    Amean = (c+d)/2
    print("The Arithmetic mean of a and b is :",Amean)
    if(Amean>30):
        print("The Amean is greater than 30 ")
    else:
        print("else in function")
def isgreater(c,d):
    if(c>d):
     print("c is greater than d")
    else:
     print("d is greater than c")    #also used if elif else 
       
def islesser(a,b): #This function is run because they used the pass statement 
    pass   # it writing resume in lab    
                  
Amean(c,d);    
# if(c>d):
#     print("c is greater than d")
# else:
#     print("d is greater than c")      
isgreater(c,d); 
islesser(a,b);  

def name(myname,Lname,Fname):
    print("Hello",myname,Lname,Fname)
    
name("shahbaz","junaid","S/o Ghulam Rasool");     
name("shahbaz","junaid","S/o Ghulam Rasool");    


def enter_Full_name(Name,lastname):
    print("My name is ",Name,lastname)
 
enter_Full_name("Shahbaz","juanid")   
