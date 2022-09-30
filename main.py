import matplotlib.pyplot as plt
import numpy as np
from itertools import islice

a,l,x,lin,xin=0,0.01,0.01,0,0
xp,yp,x_p,y_p=[],[],[],[]

while l<=4 :
    while x<=.5:
        a=x
        while xin<=50000:
            a=l*a*(1-a)
            xin+=1
            xp.append(l)
            yp.append(a)
        xin=0
        x=x+.1
    xin=0
    x=0.01
    l=l+0.01

for p in islice(yp, 0, len(yp), 500):
    y_p.append(p)
for q in islice(xp, 0, len(xp), 500):
    x_p.append(q)

print("\nNumber of x values:",len(x_p))
print("Number of y values:",len(y_p))
print('Total number of values:',len(xp))

fig, ax = plt.subplots(figsize=(8,6))
ax.scatter(x_p, y_p, color='red', marker='x', s=0.1, label='x(n+1)=a*x(n)*[1-x(n)]')
# 'fancybox=False' produces a legend box with sharp edges.
ax.legend(loc='best', frameon=True, fancybox=False)
ax.set_title('The logistic map');
plt.grid(True)
plt.show()

print("Done")