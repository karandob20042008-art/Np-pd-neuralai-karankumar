import pandas as pd
data = {"Name": ["A", "B", "C", "D", "E", "F"],   
        "Math": [80, 60, 90, 70, 85, 55],    
        "Science": [75, 65, 95, 72, 80, 60],    
        "English": [85, 70, 88, 75, 90, 50]
}
df= pd.DataFrame(data)
print(df)
average= df.loc[:,'Math':'English'].mean(axis=1)
df['Average']=average
total=df.iloc[:, 1:4].sum(axis=1)
df['Total']=total
df['Passed']=df['Average']>=60
print(df)
print(df['Average'].max())
print(df.loc[df["Average"]>80])
print(df.sort_values(by="Average", axis=0, ascending=False))
print(df["Average"].mean())
print(df.drop(columns=['Math', 'Science','English' ]))