# ---------------------- Day 58 -------------------
#                  Ramadan 17

# Constructors in python


class Person:
   
    def __init__(self,name,occupation):
     print("Hey How you")
     self.name = name
     self.occupation = occupation    
  
    def info(self):
         print(f"{self.name} is a {self.occupation}")

# a = Person()
# b = Person()
a = Person("shahbaz","DA")
b = Person("Saba","HR")
a.info()
b.info()

# print(a)
# a.name = "Saba"
# a.occupation ="HR "
# print(a.name)
# a.info() 
# b.info()