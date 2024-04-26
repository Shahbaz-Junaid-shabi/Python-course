# Make a Calculator Using match case statements

a = int(input("Enter Your 1st Number "))
b = int(input("Enter Your 2st Number "))
print("What Your Wanted to Do ?")
print("1.Addition")
print("2.subtracting")
print("3.multiplication")
print("4.division")
print("5.Modulus or reminder")
print("6.Exponential or Power ")
number = int(input("Enter What You Wanted Task Perform :"))
match number :
    case 1:
        print("The Addition of a ",a ," and b " ,b, " is =",(a+b))
    case 2:
        print("The subtracting of a ",a ," and b " ,b, " is =",(a-b))
    case 3:
        print("The multiplication of a ",a ," and b " ,b, " is =",(a*b))
    case 4:
        print("The division of a ",a ," and b " ,b, " is =",(a/b))
    case 5:
        print("The sum of a ",a ," and b " ,b, " is =",(a%b))
    case 6:
        print("The Exponential or Power of a ",a ," and b " ,b, " is =",(a**b))
    case _defaultoperation:
        print("You Enter Wrong Number ")
        
        