# ---------------------- Day 37 -------------------
#                  Ramadan 11

# finally

# Irrespeect of weather condition if Ture or false :
# Irrespect of weather what happend 

try:
    l = [10,20,30,40]
    i = int(input("Enter the index :"))
    print(l[i])
    
except:
    print("Some Error occured")    
    
finally:
    print("I am always execute")   
    
def fun1():
 try:
    l = [10,20,30,40]
    i = int(input("Enter the index :"))
    print(l[i])
    return 1
    
 except:
    print("Some Error occured") 
    return 0   
    
 finally:
    print("I am always execute")     
    
x = fun1()
print(x)    