# ---------------------- Day 14 -------------------
#                   Date  17-03-2024 
# What is intentation in python ?   
#                   -------------------
# Conditio statement(s)
# ---> if
# ---> if - else
# ---> if - elif - else
# ---> Nested-if else elif 

# ---------------------  if() statement(s) -----------------
print(" This output are if statements \n")
# Example 1 :
a = 10
if(a>=5):
    print("5 is lucky no ") 
a = int(input("Enter your Number\n")) 
if(a>0):
    print("The number is Positive \n")         
# Example 2 :
# -----------------------------------------------------    
# ---------------------  if-else statement(s) -----------------
print(" This output are if-else statements \n")  
age = int(input(" Enter your age :\n"))
if(age>=18): 
    print(" You can derive ")
else:   
    print(" You can't derive")      
    
# -----------------------------------------------------    
    
# Conditional Operators are following in give below :
# ==    equality sign 
# !=     Not equality
# >      greater than
# <       less than
# >=      greater than or equal to 
# <=       less than or equal to 
appleprice = 100
budge = 200
if (budge-appleprice>50):
    print("Alxea,add 1kg apple to the cart ")
else :
    print(" You can't buy this ")  
    
# -----------------------------------------------------    
# ------------------- if elif else statement(s) ----------------------------    
        
num = int(input(" Enter You Number \n"))
if(num==0):
    print(" Number is zero :")
elif(num>0):
    print(" Number is Positive :")
elif(num<0): 
    print(" Number is Negative :") 
else:
    print(" YOU ARE ENTER THE WRONG COMMAND")
    
# -----------------------------------------------------    
           
# ------------------- Nested if elif else statement(s) ----------------------------         

Number =int(input(" ENTER YOUR NUMBER : \n ")) 
if(Number<0):
    print(" No is -ve :") 
elif(Number>0):
    if(Number<=10):
        print(" The number is 1 b/w 10")
    elif(Number>10 and Number<=20):   
        print(" The number is 10 b/w 20") 
    else :   
        print(" The number is greater than 20 ") 
else:
    print(" Number is zero :")         
    




















