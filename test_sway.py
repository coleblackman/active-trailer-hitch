# imports
import poll_and_plot

import matplotlib.pyplot as plt
import time
import numpy as np 
import seaborn as sns
from beamngpy import BeamNGpy, Scenario, Vehicle, angle_to_quat
from beamngpy.sensors import Electrics
sns.set() 

def swerve_front(truck1, truck2, dir):
    truck1.control(dir, 1.0, None, None, None, None)
    truck2.control(dir, 1.0, None, None, None, None)

def moveHitchAndPoll(truck1, truck2, trailer1, trailer2):
    a = 0
    while a < 6:
        truck1.set_lights(right_signal=True)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        swerve_front(truck1, truck2, -1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        swerve_front(truck1, truck2, 0)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        # swerve(-1)
        truck1.set_lights(right_signal=True)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        #swerve(1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        swerve_front(truck1, truck2, 1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        swerve_front(truck1, truck2, 0)
        # swerve(1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
    # swerve(-1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        # swerve(1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        swerve_front(truck1, truck2, -1)
        truck1.set_lights(left_signal=True)    
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        swerve_front(truck1, truck2, 0)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        # swerve(1)
        truck1.set_lights(left_signal=True)  
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        # swerve(-1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        swerve_front(truck1, truck2, 1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        swerve_front(truck1, truck2, 0)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        #swerve(1)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        time.sleep(0.25)
        poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
        a+=1
        print(a)

