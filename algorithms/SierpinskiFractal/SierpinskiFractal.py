# Sierpinski triangle generator
# made by Hamza Ba-mohammed

import matplotlib.pyplot as plt
import random as rd
import yaml
import os

# Load config.yaml
config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)

heads = config.get('heads', [[1,0],[0,0],[0.5,0.66]])
y = config.get('start_point', [0.7,0])
iterations = config.get('iterations', 1000)
pause = config.get('pause', 0.05)

for pt in heads:
    plt.plot(pt[0], pt[1], '.')

for i in range(iterations):
    x = rd.choice(heads)
    z = [(x[0]+y[0])/2, (x[1]+y[1])/2]
    plt.plot(z[0], z[1], '.')
    plt.pause(pause)
    plt.title(f"iteration N°{i+1}")
    y = z

plt.show()
