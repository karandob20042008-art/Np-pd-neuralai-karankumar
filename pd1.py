import numpy as np
import pandas as pd
data={
     "Name": ["A", "B", "C", "D", "E"],    
     "Age": [20, 25, 22, 30, 28],    
     "Marks": [85, 72, 90, 65, 88],    
     "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}
df=pd.DataFrame(data)
print(df)
print("")
print(df.head(3))
print("")
print(df.head(2))
print("")
print(df.shape)
print(df.columns)
print(type(df))
print(df.loc[df['Marks']>80])
print(df.sort_values(by='Marks',axis=0, ascending=False))