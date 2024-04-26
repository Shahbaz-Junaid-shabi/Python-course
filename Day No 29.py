# ---------------------- Day 29 -------------------
#                   Date  16 - 12 -2023 
#                   ------------------


#Docstring and Pep-8 interview question

# Docstring 
"""
       python docstring are the string literals that appear right after the definition of a function ,methods,class or module
       
"""
def square(n):
    '''
    Taking square of any number :
    '''#This dot string
    print(n**2)

square(10)    

# when we want to print the docstring then use it
print(square.__doc__)
print(type(square))

# Note : Docstring write after parameter  below the function in the program 


# PEP-8 in python 

# PEP-8 provides best guideline and practices 
'''PEP 8
PEP 8 is a document that provides guidelines and
best practices on how to write Python Code. It was
written in 2001 by Guido van Rossum, Barry Warsaw,
and Nick Coghlan. The primary focus of PEP 8 is to
improve the readability and consistency of Python
PEP stands for Python Enhancement Proposal, and
there are several of them. A PEP iS a document that
new features proposed for and
documents aspects of Python. like design and style,
for the community.
'''


# What is do import this 
# import this ---> The Zen of python 

'''
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>
'''



# doc string 
def sum(a,b):
    '''
    The sum of a and b is = 
    
    '''
    print( a + b )
       
sum(5,4)    
    
# string format 
fullname = "hi I am  {} and I am from {}"
name = "Shahbaz Junaid"
village = "Saling"
print(fullname.format(name,village))
