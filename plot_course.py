import matplotlib.pyplot as plt
import time
import numpy as np 
import seaborn as sns
from beamngpy import BeamNGpy, Scenario, Vehicle, angle_to_quat
from beamngpy.sensors import Electrics
sns.set() 
import string

def average(lst): 
    return sum(lst)/len(lst)


name_list = ["moving_0.5s_", "moving_0.5s_flipped_", "moving_1.5s_", "moving_10deg_", "moving_15deg_", "moving_", "moving_car_"]
angle_list = ["moving_0.5s_", "moving_0.5s_flipped_", "moving_1.5s_", "moving_10deg_", "moving_15deg_", "moving_"]

for file_name in angle_list:
    with open(file_name+"angles.txt") as f:
        lines = f.read().splitlines()
    for i in range(0, len(lines)):
        lines[i] = int(float(lines[i]))
    print(file_name, "average:", str(average(lines)), "max:", (max(lines)))


for file_name in name_list:

    with open(file_name+"truck1_pos.txt") as f:
        lines_1 = f.read().splitlines()
    with open(file_name+"trailer1_pos.txt") as f:
        lines_2 = f.read().splitlines()
    print(lines_1)
    lines_2 = lines_1[0][0]
    x = [p[0] for p in lines_1[0]]
    y = [p[1] for p in lines_1[0]]
    plt.plot(x, y, 'g.')
    x2 = [p2[0] for p2 in lines_2[0]]
    y2 = [p2[1] for p2 in lines_2[0]]
    plt.plot(x2, y2, 'r.')
    print(len(lines_1))

plt.axis('square')
plt.show()
plt.clf()
