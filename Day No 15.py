# ---------------------- Day 15 -------------------
#                   Date  17-03-2024 

#                   -------------------

# it give the local time @codewithharry 
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)

# Make a clock using strtime()   
print("-------------------------- simple Clock ----------------------")
print("This is a program to print the now time ") 
import time
hourstime = time.strftime('%H')
print("This is show hours",hourstime)
minutestime = time.strftime('%M')
print("This is show minutes",minutestime)
secondtime = time.strftime('%S')
print("This is show second",secondtime)
timeshow = time.strftime('%H:%M:%S')
print(timeshow)
# Home given by the harry bhai 

print("-------------- THIS SIMPLE CALCULATOR ----------------")
n =15 
m = 7
ans1 = n+m
print("Addition of ",n," and ",m,      "is",(n+m))
ans2 = n-m
print("subtract of ",n," and ",m,   "is",(n-m))
ans3 = n*m
print("Multiply of ",n," and ",m,      "is",(n*m))
ans4 = n/m
print("Divsion of " ,n,   "  and ",m,       "is",(n/m))  
ans5 = n//m 
print("Floor Divison of ",n,"and",m,   "is",(n//m))
ans6 = n%m   
print("Modulus of " ,n, " and ",m,       "is",(n%m))  

# Using Date and time Modules in Python 
import time 
hours = time.strftime('%H')
print("This is show only hours :",hours)
Minutes = time.strftime('%M')
print("This is show only Minutes :",Minutes)
Second = time.strftime('%S')
print("This is only Second :",Second)

print("The below line See Exact time with Hours,Minute and also second")

timeshow = time.strftime('%H:%M:%S')
print("The Exactlly Time is ",timeshow)