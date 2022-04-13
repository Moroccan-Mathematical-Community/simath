# Sierpinski triangle generator
# made by Hamza Ba-mohammed

import matplotlib.pyplot as plt
import random as rd

heads = [[1,0],[0,0],[0.5,0.66]]
y = [0.7,0]
plt.plot(1,1,'.')
plt.plot(0,0,'.')
for i in range(1000):
    x = rd.choice(heads)
    z = [(x[0]+y[0])/2,(x[1]+y[1])/2]
    plt.plot(z[0], z[1],'.')
    plt.pause(0.05)
    plt.title("iteration N°"+str(i+1))
    y = z

plt.show()
