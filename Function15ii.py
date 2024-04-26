print("--------------load csv file  ------------------")

import pandas as pd 

df = pd.read_csv('data1.csv')
print(df.to_string())
# before finding the mean fillup the empty cell 
print("-------------------- mean() ------------------")
import pandas as pd 

df = pd.read_csv('data1.csv')
varaible = df["Duration"].fillna(60)
print(varaible.to_string())
variable1 = df["Pulse"].mean()

print(variable1)


print("-------------------- median() ------------------")
import pandas as pd 

df = pd.read_csv('data1.csv')
variable2 = df["Maxpulse"].median()

print(variable2)


print("-------------------- mode() ------------------")
import pandas as pd 

df = pd.read_csv('data1.csv')
variable3 = df["Maxpulse"].mode()[1]

print(variable3)

# print("-------------------- corr() ------------------")
# import pandas as pd 

# df = pd.read_csv('data1.csv')
# print(df.corr())
