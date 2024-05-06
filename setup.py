# install packages if needed
import subprocess
import sys
import pip
import time

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Example
if __name__ == '__main__':
    install('argh')
"""
install('matplotlib')
install('seaborn')
install('beamngpy')
install('keyboard')
install('numpy')
"""
#%matplotlib inline
import keyboard
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
from beamngpy import BeamNGpy, Scenario, ScenarioObject, Vehicle, angle_to_quat
from beamngpy.sensors import Electrics
sns.set() 

def initiateVehicles(truck1, truck2, trailer1, trailer2, map="smallgrid"):
    # setup beamNG connection
    # for demo:
    beamng = BeamNGpy('localhost', 64256, './BeamNG.tech.v0.31.3.0/BeamNG.tech.v0.31.3.0', 'C:/Users/johnl/AppData/Local/BeamNG.drive/BeamNG.tech.v0.31.3.0/BeamNG.tech.v0.31.3.0/Bin64/BeamNG.tech.x64.exe', "/Users/johnl/AppData/Local/BeamNG.drive")
    # on laptop:
    # beamng = BeamNGpy('localhost', 64256, './BeamNG.tech.v0.31.3.0/BeamNG.tech.v0.31.3.0', 'C:/Users/Student/AppData/Local/BeamNG.drive/BeamNG.tech.v0.31.3.0/BeamNG.tech.v0.31.3.0/Bin64/BeamNG.tech.x64.exe', "/Users/Student/AppData/Local/BeamNG.drive")

    beamng.open()
    vehicles = beamng.vehicles.get_available()['vehicles']
    #print(list(sorted(vehicles.keys())))
    #scenarios = beamng.scenario.get_levels()
    #print(list(sorted(scenarios.keys())))
    # add vehicles
    truck1 = Vehicle('ego', model='car_mod_2', license='TRACTOR', color='Green') # car_mod_2
    truck2 = Vehicle('ego2', model='car_mod_2', license='TRACTOR2', color='Red')
    trailer1 = Vehicle('trailer', model='boxutility')
    trailer2 = Vehicle('trailer2', model='boxutility')
    truck3 = Vehicle('ego3', model='car_mod_2', license='TRACTOR', color='Green') # car_mod_2
    truck4 = Vehicle('ego4', model='car_mod_2', license='TRACTOR2', color='Red')
    trailer3 = Vehicle('trailer3', model='boxutility')
    trailer4 = Vehicle('trailer4', model='boxutility')
    parking_plate = ScenarioObject(oid='kickplate', 
                                name='kickplate',
                                otype='BeamNGVehicle',
                                pos=(10, 20, 0),
                                rot_quat=angle_to_quat((0,0,90)),
                                scale=(1, 1, 1),
                                JBeam='kickplate',
                                datablock='default_vehicle')
    bar1 = ScenarioObject(oid='roadblock', 
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
    truck3.sensors.attach('electrics', electrics)
    truck4.sensors.attach('electrics', electrics)
    trailer3.sensors.attach('electrics', electrics)
    trailer4.sensors.attach('electrics', electrics)
    # create our scenario 
    scenario = Scenario(map, 'vehicle_state') # [543.2596940113453, -154.43656356395877, 146.73562960569507]
    if map == "west_coast_usa" :              # [467.5345010551173, -106.53487611485252, 146.01402042508562]
        scenario.scene                  
        scenario.add_vehicle(truck1, pos=(543.2596940113453, -158.43656356395877, 146.73562960569507), rot_quat=angle_to_quat((0, 0, 90))) #old z:118.675
        scenario.add_vehicle(truck2, pos=(543.2596940113453, -154.43656356395877, 146.73562960569507), rot_quat=angle_to_quat((0, 0, 90))) #old z:118.675
        scenario.add_vehicle(trailer1, pos=(549.2596940113453, -158.43656356395877, 146.73562960569507), rot_quat=angle_to_quat((0,0,90)))
        scenario.add_vehicle(trailer2, pos=(549.2596940113453, -154.43656356395877, 146.73562960569507), rot_quat=angle_to_quat((0,0,90)))
        scenario.add_vehicle(truck4, pos=(473.5345010551173, -102.53487611485252, 146.01402042508562), rot_quat=angle_to_quat((0, 0, 270))) #old z:118.675
        scenario.add_vehicle(truck3, pos=(473.5345010551173, -106.53487611485252, 146.01402042508562), rot_quat=angle_to_quat((0, 0, 270))) #old z:118.675
        scenario.add_vehicle(trailer3, pos=(467.5345010551173, -102.53487611485252, 146.01402042508562), rot_quat=angle_to_quat((0,0,270)))
        scenario.add_vehicle(trailer4, pos=(467.5345010551173, -106.53487611485252, 146.01402042508562), rot_quat=angle_to_quat((0,0,270)))
    
    else:
        scenario.scene                
        scenario.add_vehicle(truck1, pos=(5,0,0), rot_quat=angle_to_quat((0, 0, 0))) #old z:118.675
        scenario.add_vehicle(truck2, pos=(20, 0, 0), rot_quat=angle_to_quat((0, 0, 0))) #old z:118.675
        scenario.add_vehicle(trailer1, pos=(5, 6.25, 0), rot_quat=angle_to_quat((0,0,0)))
        scenario.add_vehicle(trailer2, pos=(20, 6.25, 0), rot_quat=angle_to_quat((0,0,0)))
        scenario.add_object(bar1)

    scenario.make(beamng)
    # load scenario
    beamng.scenario.load(scenario)
    print("loaded scenario")
    print("about to start")
    # keyboard.press_and_release('c')  # Press 'c' key
    time.sleep(5)
    keyboard.press_and_release('l')  # Press 'l' key
    time.sleep(5)
    beamng.scenario.start() 
    print("just started")
    truck1.set_license_plate('Hitch')
    truck1.set_shift_mode('arcade')
    truck1.ai.set_mode('span')
    truck2.ai.set_mode('stop')
    trailer1.ai.set_mode('span')
    trailer2.ai.set_mode('stop')
    truck3.set_license_plate('Hitch')
    truck3.set_shift_mode('arcade')
    truck3.ai.set_mode('span')
    truck4.ai.set_mode('stop')
    trailer3.ai.set_mode('span')
    trailer4.ai.set_mode('stop')
    return truck1, truck2, trailer1, trailer2, truck3, truck4, trailer3, trailer4


        
