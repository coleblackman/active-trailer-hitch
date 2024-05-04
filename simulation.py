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
sns.set() 

# add vehicles
truck1 = Vehicle('ego', model='car_mod_2', license='TRACTOR', color='Green')
truck2 = Vehicle('ego2', model='car_mod_2', license='TRACTOR2', color='Red')
trailer1 = Vehicle('trailer', model='boxutility')
trailer2 = Vehicle('trailer2', model='boxutility')
# trying to use function to make setup easier
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)

#manually connect the trailers and trucks in the beamNG game
time.sleep(10)

#print initial positions, directions
truck1.sensors.poll()
truck1_sensors = truck1.sensors
truck2.sensors.poll()
truck2_sensors = truck2.sensors
print('Position of Truck1')
print(truck1.state['pos'])
print('Direction of Truck1')
print(truck1.state['dir'])
print('Position of Truck2')
print(truck2.state['pos'])
print('Direction of Truck2')
print(truck2.state['dir'])

def swerve(dir):
    truck1.control(dir, 1.0, None, None, None, -1)
    truck2.control(dir, 1.0, None, None, None, -1)

def angle_between(head, trailer, in_degrees=True):
    """Calculate the angle between two vectors."""
    # Calculate dot product
    dot_product = sum(a*b for a, b in zip(head, trailer))
    # Calculate magnitudes
    magnitude_head = math.sqrt(sum(a**2 for a in head))
    magnitude_trailer = math.sqrt(sum(b**2 for b in trailer))
    # Calculate cosine of the angle
    cosine_angle = dot_product / (magnitude_head * magnitude_trailer)
    # Convert cosine to angle in radians
    angle_rad = math.acos(cosine_angle)
    if in_degrees:
        # Convert radians to degrees
        return math.degrees(angle_rad)
    else:
        return angle_rad
def heading_to_angle(heading_vector):
    # Normalize the vector to make sure it has unit length
    heading_vector = np.array(heading_vector)
    heading_vector /= np.linalg.norm(heading_vector)
    
    # Compute the angle in radians using arctan2
    angle_radians = np.arctan2(heading_vector[1], heading_vector[0])
    
    # Convert radians to degrees
    angle_degrees = np.degrees(angle_radians)
    
    # Ensure angle is between 0 and 360 degrees
    angle_degrees = angle_degrees % 360
    
    return angle_degrees
# set speed to 25m/s for testing sway
truck1.ai_set_speed(25)
truck2.ai_set_speed(25)

# set speed to -1m/s for testing reverse
#truck1.ai_set_speed(1)
#truck2.ai_set_speed(1)

#run the simulation


count =0
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
truck1.control(0, 0.1, None, None, None, -1)
time.sleep(2)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, -1)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

time.sleep(0.3)
print(count)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

print("reverse straight")


truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

print(count)
print("back")
count+=1
truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

print(count)
print("back")
count+=1
truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, -1)
time.sleep(0.0)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

print(count)
print("back")
count+=1

truck1.control(0, 0.0, None, None, None, 0)
time.sleep(1.5)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

print(count)
print("stop")
count+=1

print("going forward and right")
truck1.control(1, 0.1, None, None, None, 2)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, 2)
time.sleep(0)
truck1.control(1, 0.1, None, None, None, 2)
time.sleep(2.0)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(1, 0.1, None, None, None, 2)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(1, 0.1, None, None, None, 2)
time.sleep(1.)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)


print("going back again")
#truck1.control(0, 0.1, None, None, None, 1)
#time.sleep(2)
truck1.control(0, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(-1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

print("back even more")
#truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

#truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

#truck1.control(1, 0.1, None, None, None, -1)

truck1.control(0, 0.1, None, None, None, 1)
time.sleep(1.0)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.0, None, None, None, 0)
time.sleep(4)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)


truck1.control(-1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(-1, 0.1, None, None, None, -1)
time.sleep(0.3)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)

truck1.control(0, 0.0, None, None, None, 0)
poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)


poll_and_plot.plot_poisitions(truck1, truck2, trailer1, trailer2)
truck1.set_shift_mode('arcade')

# truck1.control(0, 0.1, None, None, None, -1)
# time.sleep(2)
# truck1.ai_set_speed(25)
# truck2.ai_set_speed(25)

while(True):
    poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
    print(angle_between(truck1.state['dir'], trailer1.state['dir'] ))
    print(truck1.state['pos'][0], trailer1.state['pos'][0])
    print(heading_to_angle(truck1.state['dir']) , heading_to_angle(trailer1.state['dir']))
    if angle_between(truck1.state['dir'], trailer1.state['dir'] ) > 20 : #and truck1.state['pos'][0] < trailer1.state['pos'][0] :
        truck1.set_lights(right_signal=True)   
        time.sleep(1)
        truck1.set_lights(right_signal=True) 
        time.sleep(1)
        truck1.set_lights(left_signal=True)   
        time.sleep(1)
        truck1.set_lights(left_signal=True) 
        time.sleep(1)
    #elif angle_between(truck1.state['dir'], trailer1.state['dir'] ) > 10:




test_sway.moveHitchAndPoll(truck1, truck2, trailer1, trailer2)
#test_reverse.reverseAndPoll(truck1, truck2, trailer1, trailer2)

truck1.ai_set_speed(0)
truck2.ai_set_speed(0)


print("starting plots")
poll_and_plot.plot_poisitions(truck1, truck2, trailer1, trailer2)
#poll_and_plot.plot_angles(truck1, truck2, trailer1, trailer2)
print("finished plots")



# trying to connect trailers
#truck.queue_lua_command('beamstate.toggleCouplers(\'tow_hitch\')')
#"beamstate.toggleCouplers('tow_hitch', true, false, true)",
#truck.queue_lua_command('beamstate.toggleCouplers(\'tow_hitch\')')
#bngApi.activeObjectLua('electrics.values.potatoes = 1');
#truck.queue_lua_command('beamstate.toggleCouplers( ["hc", 0.0, 2.76, 0.58,{"couplerTag":"tow_hitch","couplerStrength":2001000,"couplerRadius":1}] )')
