# ---------------------- Day 16 -------------------
#                   Date  18-03-2024 
#                   -------------------
# 
# ------------------- Matchcae statement(s) -------------------
week = int(input(" Enter Number of Day \n"))
match week :
    case 1 :
        print("1. Today is Monday !")
    case 2 :   
        print("2. Today is Tuesday !")  
    case 3 :       
        print("3. Today is Wednesday !")
    case 4 :   
        print("4. Today is Thursday !")
    case 5 :      
        print("5. Today is Friday !")
    case 6 :   
        print("6. Today is Saturday !")
    case 7 :       
        print("7. Today is Sunday !")
    case _: #This is default case and we give one or more default in python 
        print(" you enter wrong no")
        
        # Make a Calculator Using match case statements

a = int(input("Enter Your 1st Number "))
b = int(input("Enter Your 2st Number "))
print("What Your Wanted to Do ?")
print("2.Addition")
print("3.subtracting")
print("4.multiplication")
print("5.division")
print("6.Modulus or reminder")
print("7.Exponential or Power ")
number = int(input("Enter What You Wanted Task Perform"))
match number :
    case 2:
        print("The sum of a ",a ," and b " ,b, " is =",(a+b))
    case 3:
        print("The sum of a ",a ," and b " ,b, " is =",(a-b))
    case 4:
        print("The sum of a ",a ," and b " ,b, " is =",(a*b))
    case 5:
        print("The sum of a ",a ," and b " ,b, " is =",(a/b))
    case 6:
        print("The sum of a ",a ," and b " ,b, " is =",(a%b))
    case 7:
        print("The sum of a ",a ," and b " ,b, " is =",(a**b))
    case _defaultoperation:
        print("You Enter Wrong Number ")       