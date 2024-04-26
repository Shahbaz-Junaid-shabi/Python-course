# ---------------------- Day 49 -------------------
#                  Ramadan 15

# file IO handling in python important


# r --> used for read()
# w --> used for wirte()
# a --> used for append()
# x --> create file 
f = open('harry.txt','r')
# print(f)
text = f.read()
print(text)
f.close()

# for write 
f = open('harry1.txt','w')
f.write("Hello World!")
f.close()

f = open('harry.txt','a')
f.write("Hello World!")
f.close()   

# with is automatically closed 
with open('harry1.txt','a')as f:
 f.write("i am inside")