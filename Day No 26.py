# ---------------------- Day 26 -------------------
#                       Ramadan 8
 
#                   ------------------

# 2nd Execrise soulution print the extact time 
import time 
time = time.strftime('%H:%M:%S')
print(time) 
time = int(input("Enter Your time :"))
if(time >= 6 and time<=12):
    print("Good Morning")
elif(time >=12 and time <= 18):
    print("Good Afternoom")   
elif(time >=18 and time <= 24):
    print("Good Night")     
    