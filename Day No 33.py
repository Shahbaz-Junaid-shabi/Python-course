# ---------------------- Day 33 -------------------
#                  Ramadan 11

#   Dictionary in python

# It is ordered collection of data items in python
# key value pairs
# It in enclosed the clurly braces{} and the value seperate with comas


dic = {" name ": "shahbaz Junaid", " Roll NO ": 222249, " subject ": "programming"}

print(dic)
print(type(dic))


dic1 = {49: "shahbaz Junaid", 50: "jamil Ahmad", 51: " zeeshan Ali"}

# key()
print(dic1.keys())


print(dic1)
print(dic1[51])


#  get use

print(dic1.get(4))  # print None
print(dic1.get(49))

print(dic1.keys())

for key in dic1.keys():
    print(dic1[key])
    print(f"The value of coresponding to the {key} is {dic1[key]}  ")


# items()
print(dic.items())
