# imports
import setup
import poll_and_plot
import test_sway
import test_reverse
import matplotlib.pyplot as plt
import time
import numpy as np 
import seaborn as sns
from beamngpy import BeamNGpy, Scenario, Vehicle, angle_to_quat
from beamngpy.sensors import Electrics
import math
import threading
import pip
import time
import angle_math
import keyboard
sns.set() 

# add vehicles
truck1 = Vehicle('ego', model='car_mod_2', license='TRACTOR', color='Green')
truck2 = Vehicle('ego2', model='car_mod_2', license='TRACTOR2', color='Red')
trailer1 = Vehicle('trailer', model='boxutility_loaded_200')
trailer2 = Vehicle('trailer2', model='boxutility')
# trying to use function to make setup easier
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)

#manually connect the trailers and trucks in the beamNG game
"""
time.sleep(10)
keyboard.press_and_release('c')  # Press 'a' key
print("pressed c")
time.sleep(10)
keyboard.press_and_release('l')  # Press 'a' key
time.sleep(10)
"""
def swerve(dir):
    truck1.control(dir, 1.0, None, None, None, -1)
    truck2.control(dir, 1.0, None, None, None, -1)


name_list  = []
angles_list = []
truck_x_list = []
truck_y_list = []
trailer_x_list = []
trailer_y_list = []  

wait_times = [1.0]# 0.5, 1.5]
flipped = [0]# ,1]
degrees = [120, 120, 120, 15, 15, 15] # [0, 3, 5, 10, 15, 20, 120] # test degrees first

lap_time = 180
file1 = open('noHitchTruck_120_1.txt', 'w')
file2 = open('noHitchTrailer_120_1.txt', 'w')      
file5 = open('angles_120_1.txt', 'w')
truck1.ai.set_mode('span')
name = ("deg:"+str(120)+"1")
before_loop_time = time.time()
angles = []
truck_x = []
truck_y = []
trailer_x = []
trailer_y = []     
while(float(time.time()-before_loop_time) < float(lap_time)):
    print(time.time()-before_loop_time)
    truck1.sensors.poll()
    trailer1.sensors.poll()
    truck1_sensors = truck1.sensors
    trailer1_sensors = trailer1.sensors
    ang_between = angle_math.angle_between(truck1.state['dir'], trailer1.state['dir'] )
    orientation_result = angle_math.orientation(truck1.state['dir'], trailer1.state['dir'])
    angles.append(ang_between)
    truck_x.append(float(truck1.state['pos'][0]))
    truck_y.append(float(truck1.state['pos'][1]))
    trailer_x.append(float(trailer1.state['pos'][0]))
    trailer_y.append(float(trailer1.state['pos'][1]))
    file1.write(str(truck1.state['pos'])+'\n')
    file2.write(str(trailer1.state['pos'])+'\n')
    file5.write(str(ang_between)+'\n')

    if ang_between > 120 and "right"== orientation_result :
        truck1.set_lights(left_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(left_signal=False)   
    elif ang_between > 120 and "left"== orientation_result:
        truck1.set_lights(right_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(right_signal=False) 

name_list.append(name)
angles_list.append(angles)
truck_x_list.append(truck_x)
truck_y_list.append(truck_y)
trailer_x_list.append(trailer_x)
trailer_y_list.append(trailer_y)
file1.close()
file2.close()
file5.close()
# truck1.teleport(pos=(5, 0, 0), rot_quat=angle_to_quat((0, 0, 0)))
# trailer1.teleport(pos=(5, 6.25, 0), rot_quat=angle_to_quat((0, 0, 0)))
# simulate key click
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)
# keyboard.press_and_release('l')  # Press 'a' key
# time.sleep(5)


name_list  = []
angles_list = []
truck_x_list = []
truck_y_list = []
trailer_x_list = []
trailer_y_list = []  

wait_times = [1.0]# 0.5, 1.5]
flipped = [0]# ,1]
degrees = [120, 120, 120, 15, 15, 15] # [0, 3, 5, 10, 15, 20, 120] # test degrees first

lap_time = 180
file1 = open('noHitchTruck_120_2.txt', 'w')
file2 = open('noHitchTrailer_120_2.txt', 'w')      
file5 = open('angles_120_2.txt', 'w')
truck1.ai.set_mode('span')
name = ("deg:"+str(120)+"2")
before_loop_time = time.time()
angles = []
truck_x = []
truck_y = []
trailer_x = []
trailer_y = []     
while(float(time.time()-before_loop_time) < float(lap_time)):
    print(time.time()-before_loop_time)
    truck1.sensors.poll()
    trailer1.sensors.poll()
    truck1_sensors = truck1.sensors
    trailer1_sensors = trailer1.sensors
    ang_between = angle_math.angle_between(truck1.state['dir'], trailer1.state['dir'] )
    orientation_result = angle_math.orientation(truck1.state['dir'], trailer1.state['dir'])
    angles.append(ang_between)
    truck_x.append(float(truck1.state['pos'][0]))
    truck_y.append(float(truck1.state['pos'][1]))
    trailer_x.append(float(trailer1.state['pos'][0]))
    trailer_y.append(float(trailer1.state['pos'][1]))
    file1.write(str(truck1.state['pos'])+'\n')
    file2.write(str(trailer1.state['pos'])+'\n')
    file5.write(str(ang_between)+'\n')

    if ang_between > 120 and "right"== orientation_result :
        truck1.set_lights(left_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(left_signal=False)   
    elif ang_between > 120 and "left"== orientation_result:
        truck1.set_lights(right_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(right_signal=False) 

name_list.append(name)
angles_list.append(angles)
truck_x_list.append(truck_x)
truck_y_list.append(truck_y)
trailer_x_list.append(trailer_x)
trailer_y_list.append(trailer_y)
file1.close()
file2.close()
file5.close()
# truck1.teleport(pos=(5, 0, 0), rot_quat=angle_to_quat((0, 0, 0)))
# trailer1.teleport(pos=(5, 6.25, 0), rot_quat=angle_to_quat((0, 0, 0)))
# simulate key click
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)
# keyboard.press_and_release('l')  # Press 'a' key
# time.sleep(5)
name_list  = []
angles_list = []
truck_x_list = []
truck_y_list = []
trailer_x_list = []
trailer_y_list = []  

wait_times = [1.0]# 0.5, 1.5]
flipped = [0]# ,1]
degrees = [120, 120, 120, 15, 15, 15] # [0, 3, 5, 10, 15, 20, 120] # test degrees first

lap_time = 180
file1 = open('noHitchTruck_120_3.txt', 'w')
file2 = open('noHitchTrailer_120_3.txt', 'w')     
file5 = open('angles_120_3.txt', 'w')
truck1.ai.set_mode('span')
name = ("deg:"+str(120)+"3")
before_loop_time = time.time()
angles = []
truck_x = []
truck_y = []
trailer_x = []
trailer_y = []     
while(float(time.time()-before_loop_time) < float(lap_time)):
    print(time.time()-before_loop_time)
    truck1.sensors.poll()
    trailer1.sensors.poll()
    truck1_sensors = truck1.sensors
    trailer1_sensors = trailer1.sensors
    ang_between = angle_math.angle_between(truck1.state['dir'], trailer1.state['dir'] )
    orientation_result = angle_math.orientation(truck1.state['dir'], trailer1.state['dir'])
    angles.append(ang_between)
    truck_x.append(float(truck1.state['pos'][0]))
    truck_y.append(float(truck1.state['pos'][1]))
    trailer_x.append(float(trailer1.state['pos'][0]))
    trailer_y.append(float(trailer1.state['pos'][1]))
    file1.write(str(truck1.state['pos'])+'\n')
    file2.write(str(trailer1.state['pos'])+'\n')
    file5.write(str(ang_between)+'\n')

    if ang_between > 120 and "right"== orientation_result :
        truck1.set_lights(left_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(left_signal=False)   
    elif ang_between > 120 and "left"== orientation_result:
        truck1.set_lights(right_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(right_signal=False) 

name_list.append(name)
angles_list.append(angles)
truck_x_list.append(truck_x)
truck_y_list.append(truck_y)
trailer_x_list.append(trailer_x)
trailer_y_list.append(trailer_y)
file1.close()
file2.close()
file5.close()
# truck1.teleport(pos=(5, 0, 0), rot_quat=angle_to_quat((0, 0, 0)))
# trailer1.teleport(pos=(5, 6.25, 0), rot_quat=angle_to_quat((0, 0, 0)))
# simulate key click
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)
# keyboard.press_and_release('l')  # Press 'a' key
# time.sleep(5)
name_list  = []
angles_list = []
truck_x_list = []
truck_y_list = []
trailer_x_list = []
trailer_y_list = []  

wait_times = [1.0]# 0.5, 1.5]
flipped = [0]# ,1]
degrees = [120, 120, 120, 15, 15, 15] # [0, 3, 5, 10, 15, 20, 120] # test degrees first

lap_time = 180
file1 = open('withHitchTruck_15_1.txt', 'w')
file2 = open('withHitchTrailer_15_1.txt', 'w')    
file5 = open('angles_15_1.txt', 'w')
truck1.ai.set_mode('span')
name = ("deg:"+str(15)+"1")
before_loop_time = time.time()
angles = []
truck_x = []
truck_y = []
trailer_x = []
trailer_y = []     
while(float(time.time()-before_loop_time) < float(lap_time)):
    print(time.time()-before_loop_time)
    truck1.sensors.poll()
    trailer1.sensors.poll()
    truck1_sensors = truck1.sensors
    trailer1_sensors = trailer1.sensors
    ang_between = angle_math.angle_between(truck1.state['dir'], trailer1.state['dir'] )
    orientation_result = angle_math.orientation(truck1.state['dir'], trailer1.state['dir'])
    angles.append(ang_between)
    truck_x.append(float(truck1.state['pos'][0]))
    truck_y.append(float(truck1.state['pos'][1]))
    trailer_x.append(float(trailer1.state['pos'][0]))
    trailer_y.append(float(trailer1.state['pos'][1]))
    file1.write(str(truck1.state['pos'])+'\n')
    file2.write(str(trailer1.state['pos'])+'\n')
    file5.write(str(ang_between)+'\n')

    if ang_between > 15 and "right"== orientation_result :
        truck1.set_lights(left_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(left_signal=False)   
    elif ang_between > 15 and "left"== orientation_result:
        truck1.set_lights(right_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(right_signal=False) 

name_list.append(name)
angles_list.append(angles)
truck_x_list.append(truck_x)
truck_y_list.append(truck_y)
trailer_x_list.append(trailer_x)
trailer_y_list.append(trailer_y)
file1.close()
file2.close()
file5.close()
# truck1.teleport(pos=(5, 0, 0), rot_quat=angle_to_quat((0, 0, 0)))
# trailer1.teleport(pos=(5, 6.25, 0), rot_quat=angle_to_quat((0, 0, 0)))
# simulate key click
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)
# keyboard.press_and_release('l')  # Press 'a' key
# time.sleep(5)
name_list  = []
angles_list = []
truck_x_list = []
truck_y_list = []
trailer_x_list = []
trailer_y_list = []  

wait_times = [1.0]# 0.5, 1.5]
flipped = [0]# ,1]
degrees = [120, 120, 120, 15, 15, 15] # [0, 3, 5, 10, 15, 20, 120] # test degrees first

lap_time = 180
file1 = open('withHitchTruck_15_2.txt', 'w')
file2 = open('withHitchTrailer_15_2.txt', 'w')      
file5 = open('angles_15_2.txt', 'w')
truck1.ai.set_mode('span')
name = ("deg:"+str(15)+"2")
before_loop_time = time.time()
angles = []
truck_x = []
truck_y = []
trailer_x = []
trailer_y = []     
while(float(time.time()-before_loop_time) < float(lap_time)):
    print(time.time()-before_loop_time)
    truck1.sensors.poll()
    trailer1.sensors.poll()
    truck1_sensors = truck1.sensors
    trailer1_sensors = trailer1.sensors
    ang_between = angle_math.angle_between(truck1.state['dir'], trailer1.state['dir'] )
    orientation_result = angle_math.orientation(truck1.state['dir'], trailer1.state['dir'])
    angles.append(ang_between)
    truck_x.append(float(truck1.state['pos'][0]))
    truck_y.append(float(truck1.state['pos'][1]))
    trailer_x.append(float(trailer1.state['pos'][0]))
    trailer_y.append(float(trailer1.state['pos'][1]))
    file1.write(str(truck1.state['pos'])+'\n')
    file2.write(str(trailer1.state['pos'])+'\n')
    file5.write(str(ang_between)+'\n')

    if ang_between > 15 and "right"== orientation_result :
        truck1.set_lights(left_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(left_signal=False)   
    elif ang_between > 15 and "left"== orientation_result:
        truck1.set_lights(right_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(right_signal=False) 

name_list.append(name)
angles_list.append(angles)
truck_x_list.append(truck_x)
truck_y_list.append(truck_y)
trailer_x_list.append(trailer_x)
trailer_y_list.append(trailer_y)
file1.close()
file2.close()
file5.close()
# truck1.teleport(pos=(5, 0, 0), rot_quat=angle_to_quat((0, 0, 0)))
# trailer1.teleport(pos=(5, 6.25, 0), rot_quat=angle_to_quat((0, 0, 0)))
# simulate key click
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)
# keyboard.press_and_release('l')  # Press 'a' key
# time.sleep(5)
name_list  = []
angles_list = []
truck_x_list = []
truck_y_list = []
trailer_x_list = []
trailer_y_list = []  

wait_times = [1.0]# 0.5, 1.5]
flipped = [0]# ,1]
degrees = [120, 120, 120, 15, 15, 15] # [0, 3, 5, 10, 15, 20, 120] # test degrees first

lap_time = 180
file1 = open('withHitchTruck_15_3.txt', 'w')
file2 = open('withHitchTrailer_15_3.txt', 'w')    
file5 = open('angles_15_3.txt', 'w')
truck1.ai.set_mode('span')
name = ("deg:"+str(15)+"3")
before_loop_time = time.time()
angles = []
truck_x = []
truck_y = []
trailer_x = []
trailer_y = []     
while(float(time.time()-before_loop_time) < float(lap_time)):
    print(time.time()-before_loop_time)
    truck1.sensors.poll()
    trailer1.sensors.poll()
    truck1_sensors = truck1.sensors
    trailer1_sensors = trailer1.sensors
    ang_between = angle_math.angle_between(truck1.state['dir'], trailer1.state['dir'] )
    orientation_result = angle_math.orientation(truck1.state['dir'], trailer1.state['dir'])
    angles.append(ang_between)
    truck_x.append(float(truck1.state['pos'][0]))
    truck_y.append(float(truck1.state['pos'][1]))
    trailer_x.append(float(trailer1.state['pos'][0]))
    trailer_y.append(float(trailer1.state['pos'][1]))
    file1.write(str(truck1.state['pos'])+'\n')
    file2.write(str(trailer1.state['pos'])+'\n')
    file5.write(str(ang_between)+'\n')

    if ang_between > 15 and "right"== orientation_result :
        truck1.set_lights(left_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(left_signal=False)   
    elif ang_between > 15 and "left"== orientation_result:
        truck1.set_lights(right_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck1.set_lights(right_signal=False) 

name_list.append(name)
angles_list.append(angles)
truck_x_list.append(truck_x)
truck_y_list.append(truck_y)
trailer_x_list.append(trailer_x)
trailer_y_list.append(trailer_y)
file1.close()
file2.close()
file5.close()
# truck1.teleport(pos=(5, 0, 0), rot_quat=angle_to_quat((0, 0, 0)))
# trailer1.teleport(pos=(5, 6.25, 0), rot_quat=angle_to_quat((0, 0, 0)))
# simulate key click
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)
# keyboard.press_and_release('l')  # Press 'a' key
# time.sleep(5)



ii=0
colors = ["b", "g", "y", "r", "o", "k", "c","b", "g", "y", "r", "o", "k", "c","b", "g", "y", "r", "o", "k", "c","b", "g", "y", "r", "o", "k", "c"]
while(ii<len(angles_list)):
    print(name_list[ii],"average:", str(sum(angles_list[ii])/len(angles_list[ii])), "max:", (max(angles_list[ii])))
        #plot position for all vehicles
    x = truck_x_list[ii]
    y = truck_y_list[ii]
    plt.plot(x, y, colors[ii])
    x1 = trailer_y_list[ii]
    y1 = trailer_y_list[ii]
    plt.plot(x1, y1, colors[ii])
    print(name_list[ii], colors[ii])
    ii+=1
plt.axis('square')
plt.show()
plt.clf()
