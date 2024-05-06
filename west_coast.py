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
import keyboard
import angle_math
sns.set() 

# add vehicles
truck1 = Vehicle('ego', model='car_mod_2', license='TRACTOR', color='Green')
truck2 = Vehicle('ego2', model='car_mod_2', license='TRACTOR2', color='Red')
trailer1 = Vehicle('trailer', model='boxutility_loaded_200')
trailer2 = Vehicle('trailer2', model='boxutility')
truck3 = Vehicle('ego3', model='car_mod_2', license='TRACTOR', color='Green')
truck4 = Vehicle('ego4', model='car_mod_2', license='TRACTOR2', color='Red')
trailer3 = Vehicle('trailer3', model='boxutility_loaded_200')
trailer4 = Vehicle('trailer4', model='boxutility')
# trying to use function to make setup easier
truck1, truck2, trailer1, trailer2, truck3, truck4, trailer3, trailer4 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2,"west_coast_usa")
    
truck1.ai.set_mode('stop')
truck2.ai.set_mode('stop')
truck1.set_shift_mode('arcade')
truck2.set_shift_mode('arcade')
truck3.ai.set_mode('stop')
truck4.ai.set_mode('stop')
truck3.set_shift_mode('arcade')
truck4.set_shift_mode('arcade')

print("begin driving")
before_loop_time = time.time()
while(float(time.time()-before_loop_time) < 600):
    truck1.sensors.poll()
    trailer1.sensors.poll()
    truck1_sensors = truck1.sensors
    trailer1_sensors = trailer1.sensors
    ang_between = angle_math.angle_between(truck1.state['dir'], trailer1.state['dir'] )
    orientation_result = angle_math.orientation(truck1.state['dir'], trailer1.state['dir'])
    truck3.sensors.poll()
    trailer3.sensors.poll()
    truck3_sensors = truck1.sensors
    trailer3_sensors = trailer1.sensors
    ang_between2 = angle_math.angle_between(truck3.state['dir'], trailer3.state['dir'] )
    orientation_result2 = angle_math.orientation(truck3.state['dir'], trailer3.state['dir'])
    
    # truck 1 will asjust for reverse
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

    # flip the direction of hitch movement for sway
    if ang_between2 > 15 and "right"== orientation_result2 :
        truck3.set_lights(left_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck3.set_lights(left_signal=False)   
    elif ang_between2 > 15 and "left"== orientation_result2:
        truck3.set_lights(right_signal=True)   
        start_time = time.time()
        while(time.time()-start_time <= 1.0):
            aaa = 0 
        truck3.set_lights(right_signal=False) 


    #print(truck1.state['pos'])
    #print(truck1.state['dir'])
    #poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
#poll_and_plot.plot_poisitions(truck1, truck2, trailer1, trailer2)