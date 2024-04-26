# ---------------------- Day 50 -------------------
#                  Ramadan 16

# read() and readlines()

# readline
f = open("myfile.txt","r")
i = 0
while True:
    line =f.readline()
    i = i + 1
    if not line:
        break
    print(line)
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    
    print(f"Marks of student {i} in Math is {m1}")
    print(f"Marks of student {i} in Math is {m2}")
    print(f"Marks of student {i} in Math is {m3}")
    
    # write 
    
f = open("myfile2.txt","w") 
lines = ["line1\n","line2\n","line3\n"]
f.writelines(lines)
f.close()   
    