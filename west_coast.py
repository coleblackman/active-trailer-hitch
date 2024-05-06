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


before_loop_time = time.time()
while(float(time.time()-before_loop_time) < 600):
    truck1.sensors.poll()
    truck1_sensors = truck1.sensors
    print(truck1.state['pos'])
    print(truck1.state['dir'])
    poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
poll_and_plot.plot_poisitions(truck1, truck2, trailer1, trailer2)