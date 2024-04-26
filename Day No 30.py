  # ---------------------- Day 30 -------------------
#                   Ramadan 10
#                   ------------------

#  Recursion in python 
'''
Recursion in python
Recursion is the process of defining something in terms
of itself.
A physical world example would be to place two parallel
mirrors facing each other. Any object in between them
would be reflected recursively.
Python Recursive Function
In Python, we know that a function can call other
functions. It is even possible for the function to call
itself. These of construct are termed as recursive
functions.
'''
# Example:

def factorial(n):
    if(n==0 or n == 1):
     return 1
    else :
        return n * factorial(n-1)
    
print(factorial(5))


# Fibonacii Sequence 
# Quick Quiz: Write a program to print the a fibonacci Sequence

'''
 f(0)=0
 f(1)=1
 f(2)=2
 f(n)=f(n-1)+f(n-2)
'''

def fibonacii(fib):
    if(fib==0):
        return 0
    elif(fib==1):
        return 1
    elif(fib == 2):
        return 2
    else:
        return fibonacii(fib -1 ) + fibonacii(fib -2)
    
print(fibonacii(5))    
    
    
# Here the fibonacii sequence program in python    


# Recrision 

def factorials(n):
    if (n == 0 or n == 1):
     return 1
    else:
        return n * factorials(n-1)

print("The Factorial of 4 is ",factorials(4))    
print("The Factorial of 5 is ",factorials(5))    
print("The Factorial of 6 is ",factorials(6))    
    
    # factorial zero and one is equal 1.
    # factorial how recall 
    # n * Factorials(n-1)
    # 4 * Factorials(4-1)
    # 3 * Factorials(3-1)
    # 2 * Factorials(2-1)
    # 1 * Factorials(1-1)
    
    
def fibonaciz(f):
    if (f == 0):
        return 0
    elif (f == 1):
        return 1
    elif (f ==2):
        return 2
    else :
        return fibonaciz(f-1) + fibonaciz(f-2)
     
print(fibonaciz(5))    