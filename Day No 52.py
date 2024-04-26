# ---------------------- Day 52 -------------------
#                  Ramadan 16

# Lambda function in python
def double(n):
    return n*2

print(double(5))


# Lambda fucntion 

# lambda arguments : experssion 

vairable1 = lambda x : x * 2
# this is called lambda function
print(vairable1(4)) 


cube = lambda x : x**2
print(cube(3))

# also make average mean and std etc

def apply(fx,value):
    return (6 + fx(value))

print(apply(cube,5))