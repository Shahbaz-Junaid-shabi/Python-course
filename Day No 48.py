# ---------------------- Day 48 -------------------
#                  Ramadan 14

# Local and global Variables 

x = 4

print(x)

def value():
    x = 5
    print(x)
    
value()  

# if we want to access the local variable as a global then use global
x = 5
def value():
    global x
    x = 4
    
    print(x)
    
value() 
  