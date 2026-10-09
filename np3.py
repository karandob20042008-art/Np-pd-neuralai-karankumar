import numpy as np
#question three

z=np.array([[25,50000],
            [17,30000],
            [35,80000],
            [42,90000],
            [19,25000],
            [31,70000]])
age= z[:,0]
a=np.where(age>=25)
print(a)
print("")
salary= z[:,1]
b=np.where(salary>=60000)
print(b)
cond1=age>=25
cond2= salary>=60000
print("")
both= cond1 & cond2
print(np.where(both))
print("")
newsal= np.where(z[:,1]<30000, 30000, z[:,1])
print(newsal)
print("")
newsalarr=np.array(newsal)
print(np.mean(newsalarr))
print("")
print(np.mean(z[z[:,0]>=25,1]))