# ---------------------- Day 46 -------------------
#                  Ramadan 13
    
# OS Module in python 
import os 
os.mkdir("100 Day of Python")

for i in range(0,100):
    os.mkdir(f"100 Day of Python/Day No {i+1}")


# import os 
# os.mkdir("DAYS")

# for i in range(0,100): 
#     os.mkdir(f"DAYS/Day No {i+1}")

import os 
folders = os.listdir("DAYS")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"DAYS/{folder}"))    