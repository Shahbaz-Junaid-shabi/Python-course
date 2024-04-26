# ---------------------- Day 19 -------------------
#                  Date  19-03-2024 
#                   -------------------
#  *****************  Break and continue Statements ***************
#*******************  Break statements in python ******************
'''
The break statements enable a program tp skip over a part of the code.
A break statements terminate the very loop to it lies within.

'''

for i in range(10):
    print("5 x", i+1, "=", 5*(i+1))     
    if(i==5):
        break
print("exit from the loop")

#*******************  Continue statements in python ******************

"""
The continue statements of the loop (particular) skiped the particular iteration .But execution remain code . 
"""
for i in range(1,10):
    print(i)
    if(i== 5): 
        print("skiped the iteration ")
        continue
    if(i== 8): 
        print("Give the special case in 8 ")    
        continue
print("exit form the continue statements") 

print("Print the 1 to 100")
for i in range(1,101,1):
    print(i) 
    if(i==50):
     break
else:
     print("Missprint")  
print("Thank you so much")    
    
    
for i in range(10):
    if(i==7):
        print("skip the iteration 7")
        continue  
    print(i)
      
for i in range(1,11):
    if(i==5): 
        print("skiped the iteration 5")
        continue
    print(i)
    
print("exit form the continue statements") 

for i in range(10):
    if(i == 5): 
        print("skip the iteration 5") 
        continue
    print("5 x", i, "=", 5*(i)) 
        
    
    # continue
for i in range(1,13):
        if (i == 10):
                print("skip the iteration")
                continue
        print(i)    