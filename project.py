import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

def fun3(m,th,y):
    ar=[]
    for i in range(5):
        ar1=[]
        for j in range(25):
            if m[i][j]>th:
                ar1.append(1)
            else:
                ar1.append(0)
        ar.append(ar1)
    ps=[]
    pf=[]
    for i in range(5):
        for j in range(25):
            if y[i][j]==ar[i][j]:
                ps.append(1)
                pf.append(0)
            else:
                ps.append(0)
                pf.append(1)
    z2=sum(ps)/125
    z3=sum(pf)/125
    z=((sum(ps))/125)+1-((sum(pf))/125)
    z4=[]
    z4.append(z)
    z4.append(z2)
    z4.append(z3)
    
    return z4
    
def fun(x,n):
    for i in range(len(n)):
        x.append(n[i])
    return x
def fun1(s):
    k=[]
    for i in range(s):
        k.append((random.randint(0,10))/10)
    return k

d=pd.read_csv('dataset1.csv')
p=d.values.tolist()
np.array(p).reshape(5,9)
n=[]
for i in range(9):
    for j in range(5):
        if p[i][j]  not in n:
             n.append(p[i][j])
s=len(n)

x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
k1=[]
k2=[]
k3=[]
k4=[]
k5=[]
x1.append('Fever')
x2.append('Cough')
x3.append('Headache')
x4.append('Sweating')
x5.append('Chest pain')
x1=fun(x1,n)
k1=fun1(s)
x2=fun(x2,n)
k2=fun1(s)
x3=fun(x3,n)
k3=fun1(s)
x4=fun(x4,n)
k4=fun1(s)
x5=fun(x5,n)
k5=fun1(s)
m=[]
m.append(k1)
m.append(k2)
m.append(k3)
m.append(k4)
m.append(k5)
y=[]
for i in range(5):
    y1=[]
    for j in range(25):
        y1.append(0)
    y.append(y1)
np.array(p)
p=np.array(p).reshape(5,9)
for j in range(9):
    
    for i in range(5):
        for k in range(25):
            if n[k] in p[i][j]:
                y[i][k]=1
zs=[]
zf=[]
zm=[]
zt=[]
z=0
z1=0
thh=[]
th=0.1
thh.append(th)
zt=fun3(m,th,y)
z=zt[0]
zs.append(zt[1])
zf.append(zt[2])
t2=(z-z1)

z1=z
th=th+0.2
thh.append(th)
zt=fun3(m,th,y)

z=zt[0]
zs.append(zt[1])
zf.append(zt[2])
t2=z-z1
th=th+0.2
while t2>=0.001 and th<=1:

    zt=[]
    z1=z
    
    thh.append(th)
    zt=fun3(m,th,y)
    z=zt[0]

    zs.append(zt[1])
    
    
    zf.append(zt[2])
    t2=(z-z1)/10
    th=th+0.2

print("Probability of Successful detection  ",zs)
print("Probability of Failure in Detection ",zf)

plt.plot(thh,zs,label='Plot showing probability of success in detection with increasing threshold')
plt.xlabel("Threshold->")


plt.plot(thh,zf,label='Plot showing probability of failure in detection with increasing threshold')
plt.xlabel("Threshold ")
plt.ylabel("Probability of success/failure in; detection")
plt.legend()
plt.show()
thre=thh[len(thh)-1]
print("Best Threshold",thre)
# 'thre' is the required threshold. If any branch probability value is greater than or equal to 'thre' then it exists, else it doesn't exists.
