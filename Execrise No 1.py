#  Make a Calculator Using the User Inputs --> float(input())
a = float(input(" Enter the frist no \n "))
b = float(input(" Enter the second no \n "))    
print(" This is All Arithmetic Operator print the value user input \" float \"")
print(" Addtion ",(a+b))
print(" subtracting ",(a-b)) 
print(" multiplication ",(a*b))     
print(" division",(a/b))         
print(" Modulus' reminder ' ",(a%b))      
print(" Floor Division(It can give point/decimal value) ",(a//b))  
print("  \' Exponential operation  \'" ,(a**b)) # actualy power 

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












