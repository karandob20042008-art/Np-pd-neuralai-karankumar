import numpy as np
import pandas as pd

data = {"Age": [20, 21, None, 24, None, 30],   
        "Salary": [30000, None, 40000, 50000, None, 60000],    
        "Experience": [1, 2, 3, None, 5, 6],    
        "Department": ["CS", "IT", "CS", None, "IT", "CS"] } 
df = pd.DataFrame(data)
print(df)
print(df.isna().sum())
print((df==3000).sum())
df['Age']=df["Age"].fillna(df['Age'].median())
df['Salary']=df["Salary"].fillna(df['Salary'].median())
df['Experience']=df["Experience"].fillna(df['Experience'].median())
df['Department']=df['Department'].fillna(df['Department'].mode()[0])

print(df.isna().sum())
print(df)