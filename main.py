# a = "harry"
# print(a)
# a =235
# print(a)
# a = 1
# b = None
# c = True
# d = "shabi"
# print("The type of a is ",type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# a = "1"
# b = "2"
# # string concentenation
# print(a+b)

# print(int(a)+int(b))
# # input 
# a = input("Enter Your Name:")
# print("My name is :",a)
# # input for integer such like this 
# a = int(input("Enter also int number:"))
# print("This is a integer Nunber",a)
# # input only string such as
# a = str(input("Enter Your Full Name :"))
# print("My name is :",a)
# ------ Day N0:10-----
# # Example 
# x = input("Enter your first Number ")
# y = input("Enter your Second Number ")
# print(x+y)
# print(int(x)+int(y))
# # Example Explicit with inputs
# x = int(input("Enter your first Number "))
# y = int(input("Enter your Second Number "))
# print(x+y)
# ------ Day N0:11-----
# # Strings 
# string = "Name"
# Name = "Shahbaz"
# print(string)
# print(Name)

# apple = " I want eat an \"apple\" and this is good " #used escape seqence
# print(apple)

# # indexing 
# Name = "shabi"
# print(Name[0])
# print(Name[1])
# print(Name[2])
# print(Name[3])
# print(Name[4])
# print("using the for loop ")
# for character in Name:
#     print(character)
# ------ Day N0:12-----
#String Slicing
# Names = "shahbaz junaid shabi"
# print(Names[0:20])
# print(len(Names)) 

# ------ Day N0:13-----
# String with Operation
# Name = "shahbaz junaid"
# print(len(Name))
# print(Name.upper())
# print(Name.lower())
# print(Name)
# name = "shahbaz $$"
# print(name.rstrip('$')) #it remove the trailing characters in strings
# # replace()
# name = "shahbaz"
# print(name.replace("shahbaz","shabi"))
# print(name.replace("shahbaz","shahbaz junaid shabi"))
# #split()
# name = "shahbaz zeeshan jamil"
# print(name.split())
# # capitalize
# name = " Welcome to Our new vlog"
# print(name.capitalize())
# #centre()
# name = "shahbaz"
# print(name.center(50))
# # count("a")
# print(name.count("a"))
# # endswith()
# print(name.endswith("baz"))
# print(name.endswith("baz",3,7))
# # find()
# name = "shahbaz junaid shabi"
# print(name.find("shabi"))
# # index()
# name = "Shahbazjunaidshabi"
# print(name.index("shabi"))
# # isalum
# print(name.isalnum())
# # islower()
# print(name.islower())
# # isprintable()
# name = "shabi \n"
# print(name.isprintable())
# # isspace()
# name = "shabaz junaid"
# print(name.isspace())
# name = "   "
# print(name.isspace())
# # istitle()
# name = "shahbaz junaid shabi"
# print(name.istitle())
# # swapcase()
# print(name.swapcase())
# # title 
# name = "welcome to the another vlog"
# print(name.title())

# ------ Day N0:14-----

# age = int(input("Enter Your age ")) 
# print("Your Age is :",age)  
# if age >=18 :
#     print("Yes")
#     print("Your can Drive the Car ")
    
# else:
#     print("No")
#     print("Your Can't Drive the Car") 

# age = int(input("Enter Your age ")) 
# print(age>20)
# print(age<20)
# print(age>=20)
# print(age<=20)
# print(age==20)
# print(age!=20)

# age = int(input("Enter Your age ") )
# if (age == 0):
#     print("Number is Zero")
# elif (age > 1) :
#     print("Number Positive")
# elif (age == 111) :
#     print("Number Special")
# else:
#     print("Nega Number")     

# Nested if 
# ------------ Day N0:15 -----
        # Make a clock using strtime()   
# print("-------------------------- simple Clock ----------------------")
# print("This is a program to print the now time ") 
# import time
# hourstime = time.strftime('%H')
# print("This is show hours",hourstime)
# minutestime = time.strftime('%M')
# print("This is show minutes",minutestime)
# secondtime = time.strftime('%S')
# print("This is show second",secondtime)
# timeshow = time.strftime('%H:%M:%S')
# print(timeshow)

# Using Date and time Modules in Python 
# import time 
# hours = time.strftime('%H')
# print("This is show only hours :",hours)
# Minutes = time.strftime('%M')
# print("This is show only Minutes :",Minutes)
# Second = time.strftime('%S')
# print("This is only Second :",Second)

# print("The below line See Exact time with Hours,Minute and also second")

# timeshow = time.strftime('%H:%M:%S')
# print("The Exactlly Time is ",timeshow)

# ------------ Day N0:16 -----
# Match Case Statements

# number = int(input("Enter Your Number :"))
# match (number):
#     case 1 :
#         print("shahbaz Junaid ")
#     case 2 :
#         print("junaid")
#     case 3 :
#         print("shabi")        
#     case _:
#         print("Wrong Number")
# ------------ Day N0:17 -----
# for loop 
# name = "shahbaz junaid shabi"
# for i in name:
#     print(i)
#     if i == "d":
#         print(" S is firt character ")
# list_01 = ["red","yellow","blue","pink"]
# for list_01 in list_01: 
#     print(list_01)
#     for i in list_01:
#         print(i)
# for i in  range(10,100,2):
#     print(i)
# # ------------ Day N0:18 ---
# i = 0 
# while i < 10 :
#         print(i)
#         i = i + 1
#         if i == 5:
#                 print("hi")
# #it recall himself whenever the condition is false
# number = int(input("Enter Your Number :"))

# # ------------ Day N0:19 ---

#   
# while(i <=10):
#         number = int(input("Enter Your Number :"))  
#         print(i)  
# print('The loop is exit')
# for i in range(1,13):
#         if (i == 10):
#                 print("skip the iteration")
#                 continue
#         print(i)
        
# # ------------ Day N0:20 ---
#function 
 
a = 4 
b = 10
Amean = (a + b)/2
print(Amean) 

def Amean(c,d):
        Amean = (c + d)/2
        print(Amean)
        if (Amean > 7):
         print("hello shabi")
        else:
         print("less") 
        
def isless(c,d):
        if (c > d):
         print("hello shabi")
        else:
         print("less") 
Amean(3,4) 
isless(c=23,d=34)      
        
def isgreater(a,b):
  pass   

def Fullname(first,second):
        print("hi",first,second)
            
Fullname("shahbaz ","junaid")        
        
        
                      
               
               
               
               