# ---------------------- Day 61 -------------------
#                  Ramadan 21 

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def show(self):
        print(f"The Employee name is {self.name} id {self.id}")    


a1 = Employee("shabi",55)
a1.show()
b = Employee("junaid",72)
b.show()
c = Employee("shahbaz junaid",5172)
c.show()

class programmer(Employee):
    def showlanguage(self):
        print("The defaulf language is python")
        
        
a1 = programmer("Shahbaz junaid shabi ",55)
a1.showlanguage()
a1.show()
        