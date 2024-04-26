# ---------------------- Day 42 -------------------
#                  Ramadan 13

# Enumerate function in Python

# simple code

marks = [ 34,45,56,67,45,67,89]
index = 0
for  mark in marks:
    print(mark)
    if (index == 4):
        print("shahbaz,Awesome!")
        
    index = index + 1    
    
# enumerate function code
print("print with indexs")
marks = [ 34,45,56,67,45,67,89]
for index,mark in enumerate(marks):
    print(index,mark)
    if (index == 4):
        print("Awesome,Shahbaz")

# By default the enumerate function index 0 but you can specify a different starting by pass a argument to the enumerate function.
print("print with indexs")
marks = [ 34,45,56,67,45,67,89]
for index,mark in enumerate(marks,start = 1):
    print(index,mark)
    if (index == 4):
        print("Awesome,Shahbaz")
    