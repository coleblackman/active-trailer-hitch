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
sns.set() 

# add vehicles
truck1 = Vehicle('ego', model='car_mod_2', license='TRACTOR', color='Green')
truck2 = Vehicle('ego2', model='car_mod_2', license='TRACTOR2', color='Red')
trailer1 = Vehicle('trailer', model='boxutility_loaded_200')
trailer2 = Vehicle('trailer2', model='boxutility')
# trying to use function to make setup easier
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)

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

def orientation(vector1, vector2):
    # Compute the cross product
    cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    
    # Check the direction of the resulting vector
    if cross_product > 0:
        return 'left'
    elif cross_product < 0:
        return 'right'
    else:
        return 'collinear'
    
truck1.ai.set_mode('stop')
truck2.ai.set_mode('stop')
truck1.set_shift_mode('arcade')
truck2.set_shift_mode('arcade')

before_loop_time = time.time()
while(float(time.time()-before_loop_time) < 120):
    poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
poll_and_plot.plot_poisitions(truck1, truck2, trailer1, trailer2)

name_list  = []
angles_list = []
truck_x_list = []
truck_y_list = []
trailer_x_list = []
trailer_y_list = []  

wait_times = [0.5, 1.0, 1.5]
flipped = [0]# ,1]
degrees = [10,15] # [0, 3, 5, 10, 15, 20, 120] # test degrees first
lap_time = 120
for stall in wait_times:
    for deg in degrees:
        for flip in flipped:
            truck1.ai.set_mode('span')
            name = ("deg:"+str(deg)+"wait_time"+str(stall)+"flip"+str(flip))
            before_loop_time = time.time()
            angles = []
            truck_x = []
            truck_y = []
            trailer_x = []
            trailer_y = []            
            file1 = open(name+'angles2.txt', 'w')
            while(float(time.time()-before_loop_time) < float(lap_time)):
                print(time.time()-before_loop_time)
                truck1.sensors.poll()
                trailer1.sensors.poll()
                truck1_sensors = truck1.sensors
                trailer1_sensors = trailer1.sensors
                ang_between = angle_between(truck1.state['dir'], trailer1.state['dir'] )
                orientation_result = orientation(truck1.state['dir'], trailer1.state['dir'])
                angles.append(ang_between)
                truck_x.append(float(truck1.state['pos'][0]))
                truck_y.append(float(truck1.state['pos'][1]))
                trailer_x.append(float(trailer1.state['pos'][0]))
                trailer_y.append(float(trailer1.state['pos'][1]))
                file1.writelines(str(ang_between))
                if(flip ==0 ):
                    if ang_between > deg and "right"== orientation_result :
                        truck1.set_lights(left_signal=True)   
                        start_time = time.time()
                        while(time.time()-start_time <= stall):
                            aaa = 0 
                        truck1.set_lights(left_signal=False)   
                    elif ang_between > deg and "left"== orientation_result:
                        truck1.set_lights(right_signal=True)   
                        start_time = time.time()
                        while(time.time()-start_time <= stall):
                            aaa = 0 
                        truck1.set_lights(right_signal=False) 
                else:
                    if ang_between > deg and "left"== orientation_result :
                        truck1.set_lights(left_signal=True)   
                        start_time = time.time()
                        while(time.time()-start_time <= stall):
                            aaa = 0 
                        truck1.set_lights(left_signal=False)   
                    elif ang_between > deg and "right"== orientation_result:
                        truck1.set_lights(right_signal=True)   
                        start_time = time.time()
                        while(time.time()-start_time <= stall):
                            aaa = 0 
                        truck1.set_lights(right_signal=False) 
            name_list.append(name)
            angles_list.append(angles)
            truck_x_list.append(truck_x)
            truck_y_list.append(truck_y)
            trailer_x_list.append(trailer_x)
            trailer_y_list.append(trailer_y)
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



#test_sway.moveHitchAndPoll(truck1, truck2, trailer1, trailer2)
#test_reverse.reverseAndPoll(truck1, truck2, trailer1, trailer2)

#poll_and_plot.plot_poisitions(truck1, truck2, trailer1, trailer2)
#poll_and_plot.plot_angles(truck1, truck2, trailer1, trailer2)

# trying to connect trailers
#truck.queue_lua_command('beamstate.toggleCouplers(\'tow_hitch\')')
#"beamstate.toggleCouplers('tow_hitch', true, false, true)",
#truck.queue_lua_command('beamstate.toggleCouplers(\'tow_hitch\')')
#bngApi.activeObjectLua('electrics.values.potatoes = 1');
#truck.queue_lua_command('beamstate.toggleCouplers( ["hc", 0.0, 2.76, 0.58,{"couplerTag":"tow_hitch","couplerStrength":2001000,"couplerRadius":1}] )')
