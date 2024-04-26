# ---------------------- Day 59 -------------------
#                  Ramadan 17

# Decorators in python 


def my_function(fx):
    def mfx(*args,**kwargs):
     print("Good Morning")
     fx(*args,**kwargs)
     print("Thank for using this function ") 
    return mfx
  
@my_function   
# before perfrom the operation print "Good morning" with the help of decorators  
def hello():
    print("Hello world")


def add(a,b):
    print(a + b)
    
my_function(add(1,9))    
hello()
