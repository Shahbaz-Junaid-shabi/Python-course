# ---------------------- Day 36 -------------------
#                  Ramadan 11

# Exception Handling Or Error Handling 

# try
# except

a = input("Enter Your Number :")
print(f" The Multiplication of Table {a}")

try:
    
 for i in range(1,11):
    print(f"{int(a)} X  {int(i)} = {int(a)*int(i)}")

except Exception as input :
    print("Invalid input")    
    
    
print("some important lines")    
print("End of line")    


# another example 

try:
 number = int(input('Enter Your No :'))
 a = [6,3]
 print(a[number])
except ValueError:
    print("This is not an inetger ")
except IndexError:
    print("IndexError")
    
    #next topic Finaly Clause 