import numpy as np
#question two

y= np.array([[10,100,1000],
            [20,200,2000],
            [30,300,3000],
            [40,400,4000],
            [50,500,5000]])
meana=y.mean(axis=0)
stda=y.std(axis=0)
print("mean=", meana)
print("std= ", stda)
y_scaled= (y-meana)/stda
print(y_scaled)