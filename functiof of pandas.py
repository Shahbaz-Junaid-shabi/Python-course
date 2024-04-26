# ---------  Function No 1 --------
# ---------  to_string() --------
# Use for print long value data 


import pandas as pd 
df = pd.read_csv("data1.csv")
# print(df.to_string())
'''
# ---------  Function No 2 --------
# head() function print first 5 rows
print(df.tail())

# ---------  Function No 3 --------
# head() function print last 5 rows
print(df.tail())

# ---------  Function No 4 --------
# detail of data fie 
print(df.info()) 

# ---------  Function No 5 --------
Also detail numberic value such as mean , std and max etc
print(df.describe())

# ---------  Function No 6 --------
# This method is used yo generate a sample row and column the dataframe
print(df.sample())

# ---------  Function No 7 --------



# size = df.size
 
# # printing size 
# print("Size = {}".format(size))
size = df.size
print(f"Size = {size}")

# ---------  Function No 8 --------

import pandas as pd 
df = pd.read_csv("data.csv")
print(df)

# ---------  Function No 9 --------

uni = df["Duration"].unique()
print(uni)

# ---------  Function No 10 --------

shape = df.shape
# printing shape
print("Shape = {}".format(shape))
df["Duration"].fillna(100,inplace=True)
print(df.to_string())
print(df.loc[1])
# selecting 0th, 2nd, 4th, and 7th index rows
print(df.iloc[[0, 2, 4, 7]])

dropn = df.dropna()  
print(dropn.to_string())
'''

import pandas as pd

print(pd.options.display.max_rows)





