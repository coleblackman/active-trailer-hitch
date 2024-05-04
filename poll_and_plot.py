import matplotlib.pyplot as plt
import time
import numpy as np 
import seaborn as sns
from beamngpy import BeamNGpy, Scenario, Vehicle, angle_to_quat
from beamngpy.sensors import Electrics
sns.set() 


#make lists for truck and trailer positions
truck1_positions = list()
truck1_directions = list()
truck1_wheel_speeds = list()
truck2_positions = list()
truck2_directions = list()
truck2_wheel_speeds = list()
trailer1_positions = list()
trailer1_directions = list()
trailer1_wheel_speeds = list()
trailer2_positions = list()
trailer2_directions = list()
trailer2_wheel_speeds = list()

def pollVehicles(truck1, truck2, trailer1, trailer2):
    truck1.sensors.poll()
    truck1_sensors = truck1.sensors
    truck2.sensors.poll()
    truck2_sensors = truck2.sensors
    trailer1.sensors.poll()
    trailer1_sensors = trailer1.sensors
    trailer2.sensors.poll()
    trailer2_sensors = trailer2.sensors
    truck1_positions.append(truck1.state['pos'])
    truck1_directions.append(truck1.state['dir'])
    truck1_wheel_speeds.append(truck1_sensors['electrics']['wheelspeed'])
    truck2_positions.append(truck2.state['pos'])
    truck2_directions.append(truck2.state['dir'])
    truck2_wheel_speeds.append(truck2_sensors['electrics']['wheelspeed'])
    trailer1_positions.append(trailer1.state['pos'])
    trailer1_directions.append(trailer1.state['dir'])
    trailer1_wheel_speeds.append(trailer1_sensors['electrics']['wheelspeed'])
    trailer2_positions.append(trailer2.state['pos'])
    trailer2_directions.append(trailer2.state['dir'])
    trailer2_wheel_speeds.append(trailer2_sensors['electrics']['wheelspeed'])

def plot_poisitions(truck1, truck2, trailer1, trailer2):
    #plot position for all vehicles
    x = [p[0] for p in truck1_positions]
    y = [p[1] for p in truck1_positions]
    plt.plot(x, y, 'g.')
    x1 = [p1[0] for p1 in truck2_positions]
    y1 = [p1[1] for p1 in truck2_positions]
    plt.plot(x1, y1, 'b.')
    x2 = [p2[0] for p2 in trailer1_positions]
    y2 = [p2[1] for p2 in trailer1_positions]
    plt.plot(x2, y2, 'y.')
    x3 = [p3[0] for p3 in trailer2_positions]
    y3 = [p3[1] for p3 in trailer2_positions]
    print(trailer1_positions)
    plt.plot(x3, y3, 'r.')
    plt.axis('square')
    plt.show()
    plt.clf()
    """
    print("finished plots")
    print("lateral distance for truck with custom hitch")
    print(max(x), min(x))
    print("lateral distance for normal truck")
    print(max(x2), min(x2))
    """

def plot_angles(truck1, truck2, trailer1, trailer2):
    angles = [np.arctan2(d[1], d[0]) for d in truck1_directions]
    angles1 = [np.arctan2(d1[1], d1[0]) for d1 in truck2_directions]
    print("got truck angles")
    angles2 = [np.arctan2(d2[1], d2[0]) for d2 in trailer1_directions]
    angles3 = [np.arctan2(d3[1], d3[0]) for d3 in trailer2_directions]
    print("got trailer angles")

    r = truck1_wheel_speeds  # We simply use the speed as the radius in the radial plot
    r1 = truck2_wheel_speeds  
    r2 = trailer1_wheel_speeds  
    r3 = trailer2_wheel_speeds  
    print("starting second plot")
    plt.subplot(111, projection='polar')
    plt.scatter(angles, r, 'b.')
    plt.scatter(angles1, r1, 'g.')
    plt.scatter(angles2, r2,'r.')
    plt.scatter(angles3, r3,'y.')
    plt.show()

def saveLists(truck1, trailer1, string_name):
    file1 = open(string_name+'truck1_pos.txt', 'w')
    file1.writelines(str(truck1_positions))
    file1.close()
    file3 = open(string_name+'trailer1_pos.txt', 'w')
    file3.writelines(str(trailer1_positions))
    file3.close()
    return truck1, trailer1
