# ---------------------- Day 51 -------------------
#                  Ramadan 16

# seek()  and tell()

with open("file.txt","r") as f :
     print(type(f))
    #  Move to 10th character and print
     f.seek(10) 
    #  tell the current position 
     print(f.tell())
     data = f.read(5)
     print(data)
     
     
with open("sample.txt","w") as f :
    f.write("Hello World!")
    f.truncate(5)
with open("sample.txt","r") as f :
    print(f.read())
    
    
 
     


     
     