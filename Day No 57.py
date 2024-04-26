# ---------------------- Day 57 -------------------
#                  Ramadan 16

# Class and object in python 

class Person:
    Name = "Shahbaz Junaid"
    Occupation = "Data Analyst"
    NeWTH = 10
    def info(self):
     print(f"{self.Name} is a {self.Occupation}") 
       
a = Person()
b = Person()
a.Name ="shabi"
a.Occupation = "Data Scienists"

b.Name = "Kiynat"
b.Occupation = "Doctor"
print(a.Name,a.Occupation)    
a.info()
b.info()