import matplotlib.pyplot as plt
import numpy as np
import random
from time import sleep

plt.style.use('_mpl-gallery')


def findmiddle(a,b):
    return (a[0]+b[0])/2 , (a[1]+b[1])/2


# make the data
np.random.seed(2)
originalx = [2,8,5]
originaly = [2,2,8]

x=[]
y=[]

plt.ion()

fig, ax = plt.subplots()
fig.set_size_inches(7, 5, forward=True)
#triangle
sc = ax.scatter(originalx, originaly , s=15 , c= "black")
colors=[]
#dots
scblue = ax.scatter(x, y , s=2 , c= np.random.rand(3,))

plt.xlim(0,10)
plt.ylim(0,10)



plt.draw()




x.append(6)
y.append(6)
scblue.set_offsets(np.c_[x,y])
#fig.canvas.draw_idle()
a=0

for i in range(100000000000):
    a=np.random.choice(3)
    middledotx,middledoty=findmiddle([x[-1],y[-1]],[originalx[a],originaly[a]])
    x.append(middledotx)
    y.append(middledoty)
    scblue.set_offsets(np.c_[x,y])
    fig.canvas.draw_idle()
    plt.pause(0.000000001)
    

  
plt.waitforbuttonpress()


# plot



"""
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

"""


