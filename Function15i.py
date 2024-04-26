 
#   ---------- 15 Function of Pandas -----------

# read csv file in pandas  
'''
import pandas as pd 

df = pd.read_csv('data.csv')
print(df)

'''
# read Excel file in python 
import pandas as pd 

print("------------------- read_excel file ------------------")
import pandas as pd 

df = pd.read_excel('day3.xlsx')
print(df)
print(df.keys())

print("------------------- DataFrame(a) ----------------------")

# DataFrame 
import pandas as pd 
mydata = {
    "CARS":["BMW","Honda","Ford","Volvo"],
    "ID":[123,345,213,231]
    
} 
new_mydata = pd.DataFrame(mydata)
print(new_mydata)

# alisa -----> are an alternative name for referring the same thing

# ---> pandas = pd
# ---> Numpy = py
# ---> matplotlib = plt    etc

# Now the pandas package can be referred to as pd insted of pandas


# Series --> is like a column in a table  and 1Dimensional array holding data of any type

# Series
print("------------------- Series(a) ------------------")

import pandas as pd 

lis = [1,2,3,4,5]

newlis = pd.Series(lis)
print(newlis)

print("------------------- Series(a) ------------------")

# key() is give info about RangeIndex and datatype 
print(newlis.keys())

# Labels 
import pandas as pd 

lis = [1,2,3,4,5]

newlis = pd.Series(lis,index=["a","b","c","d","e"])
print(newlis)
print(newlis["a"])

# Dataframe --->2D data structure like a 2 dimensional array or a table with rows and columns.

print("------------------- DataFrame(a) ------------------")

import pandas as pd 
df = {
    "Player" : ["Sach","KingK","Zak"],
    "Role" : ["Master Batter","Run Machine","Speed Machine"]
    }
# df = pd.DataFrame({"Player" : ["Sach","KingK","Zak"], "Role" : ["Master Batter","Run Machine","Speed Machine"]})
print(type(df))
newdf = pd.DataFrame(df)
print(newdf)

# loc[] ----> Refer to the row index ----> this for series
# loc[[]]---->when using [],the result is a pandas Dataframe
 
# loc[] 
print("------------------- DataFrame(a) ------------------")
print(newdf.loc[0])
print(newdf.loc[1])
# loc[[]]
print(newdf.loc[[0,1,2]])

print("-------------------- labels ------------------")

# labels
import pandas as pd 
df = {
    "Player" : ["Sach","KingK","Zak"],
    "Role" : ["Master Batter","Run  ","Speed Machine"]
    }
newdfs = pd.DataFrame(df,index=["Day1","Day2","Day3"])
print(newdfs)
print(newdfs.loc["Day1"])

# max_rows() --->60
print("-------------------- max_rows ------------------")

print(pd.options.display.max_rows)

# min_row() --> 10
print("-------------------- min_rows ------------------")

print(pd.options.display.min_rows)


print("-------------------- dropna() ------------------")

# dropna()--> remove the empty cell in data file 

import pandas as pd 

df = pd.read_csv('data1.csv')
print(df.to_string())
print("------ use dropna() empty cell are remove ---------------")

newdf = df.dropna()
# if you wants to change the original file then use (inplace=True)
print(newdf.to_string())

# fillna()--->replace the empty cell with value
import pandas as pd 

df = pd.read_csv('data1.csv')
print("-------------------- fillna() ------------------")
print(df.to_string())

# fillna() is use like this also we use (inplace=True)
print("-------------------- fillna() ------------------")
newvariable = df.fillna(1300)
print(newvariable.to_string())
 
# specific name change value also  
import pandas as pd 

df = pd.read_csv('data1.csv')
print(df.to_string())

print("----- fillna() use on one column ------------------")

variable2 =df["Duration"].fillna(1400)
print(variable2)




