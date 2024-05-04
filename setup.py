# install packages if needed
import subprocess
import sys
import pip
import keyboard
import time

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Example
if __name__ == '__main__':
    install('argh')
#install('matlibplot')
#install('seaborn')
#install('beamngpy')
#%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
from beamngpy import BeamNGpy, Scenario, ScenarioObject, Vehicle, angle_to_quat
from beamngpy.sensors import Electrics
sns.set() 

def initiateVehicles(truck1, truck2, trailer1, trailer2):
    # setup beamNG connection
    beamng = BeamNGpy('localhost', 64256, './BeamNG.tech.v0.31.3.0/BeamNG.tech.v0.31.3.0', 'C:/Users/Student/AppData/Local/BeamNG.drive/BeamNG.tech.v0.31.3.0/BeamNG.tech.v0.31.3.0/Bin64/BeamNG.tech.x64.exe', "/Users/Student/AppData/Local/BeamNG.drive")
    beamng.open()
    vehicles = beamng.vehicles.get_available()['vehicles']
    #print(list(sorted(vehicles.keys())))
    #scenarios = beamng.scenario.get_levels()
    #print(list(sorted(scenarios.keys())))
    # add vehicles
    truck1 = Vehicle('ego', model='car_mod_2', license='TRACTOR', color='Green')
    truck2 = Vehicle('ego2', model='car_mod_2', license='TRACTOR2', color='Red')
    trailer1 = Vehicle('trailer', model='boxutility')
    trailer2 = Vehicle('trailer2', model='boxutility')
    parking_plate = ScenarioObject(oid='kickplate', 
                                name='kickplate',
                                otype='BeamNGVehicle',
                                pos=(10, 20, 0),
                                rot_quat=angle_to_quat((0,0,90)),
                                scale=(1, 1, 1),
                                JBeam='kickplate',
                                datablock='default_vehicle')
    """
    barrier1 = ScenarioObject(oid='cardboard_box', 
                                name='cardboard_box',
                                otype='BeamNGVehicle',
                                pos=(4.5, 6.5, 1.5),
                                rot_quat=angle_to_quat((0,0,90)),
                                scale=(1, 1, 1),
                                JBeam='cardboard_box',
                                datablock='default_vehicle')"""
    bar1 = ScenarioObject(oid='roadblock', 
                              name='sawhorse',
                              otype='BeamNGVehicle',
                              pos=(0, 0, 0),
                              rot_quat=(0, 0, 0, 1),
                              scale=(1, 1, 1),
                              JBeam='sawhorse',
                              datablock='default_vehicle')
    obj = ScenarioObject(oid='roadblock', 
                              name='sawhorse',
                              otype='BeamNGVehicle',
                              pos=(0, 0, 0),
                              rot_quat=(0, 0, 0, 1),
                              scale=(1, 1, 1),
                              JBeam='sawhorse',
                              datablock='default_vehicle')
    electrics = Electrics()
    truck1.sensors.attach('electrics', electrics)
    truck2.sensors.attach('electrics', electrics)
    trailer1.sensors.attach('electrics', electrics)
    trailer2.sensors.attach('electrics', electrics)
    # create our scenario
    scenario = Scenario('smallgrid', 'vehicle_state')
    scenario.scene 
    scenario.add_vehicle(truck1, pos=(5, 0, 0), rot_quat=angle_to_quat((0, 0, 0))) #old z:118.675
    scenario.add_vehicle(truck2, pos=(20, 0, 0), rot_quat=angle_to_quat((0, 0, 0))) #old z:118.675
    scenario.add_vehicle(trailer1, pos=(5, 6.25, 0), rot_quat=angle_to_quat((0,0,0)))
    scenario.add_vehicle(trailer2, pos=(20, 6.25, 0), rot_quat=angle_to_quat((0,0,0)))
    # scenario.add_object(parking_plate)
    #scenario.add_object(barrier1)
    scenario.add_object(bar1)
    scenario.add_object(obj)


    scenario.make(beamng)
    # load scenario
    beamng.scenario.load(scenario)
    print("loaded scenario")
    print("about to start")
    keyboard.press_and_release('c')  # Press 'a' key
    keyboard.press_and_release('l')  # Press 'a' key
    time.sleep(5)
    beamng.scenario.start() 
    print("just started")
    truck1.set_license_plate('Hitch')
    truck1.set_shift_mode('arcade')
    truck1.ai.set_mode('span')
    truck2.ai.set_mode('stop')
    trailer1.ai.set_mode('span')
    trailer2.ai.set_mode('stop')
    return truck1, truck2, trailer1, trailer2


        
