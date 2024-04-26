# ---------------------- Day 34 -------------------
#                  Ramadan 11


# Dictionary Methods in python


dic1 = {
    49: "shahbaz junaid",
    50 : "Ali Ahmed",
    51 : "jamil Ahmed"
    }
dic2= {
    52: "shahbaz junaid",
    53 : "Ali Ahmed",
    54 : "jamil Ahmed"
    }
# update()
dic1.update(dic2)
print(dic1)
print(dic1.items())


# update()
dic3= {
    52: "shahbaz junaid",
    53 : "Ali Ahmed",
    54 : "jamil Ahmed"
    }
dic3.update({54:"khalid kakar"})
print(dic3)

# clear()
dic3.clear()
print(dic3)


# pop() is use to remove the value 
dic4= {
    52: "shahbaz junaid",
    53 : "Ali Ahmed",
    54 : "jamil Ahmed"
    }

dic4.pop(53)
print(dic4)
# popitem() is use to remove the last value 
print(dic4.popitem())

# del() is raised the erroe 
del dic4
print(dic4)

