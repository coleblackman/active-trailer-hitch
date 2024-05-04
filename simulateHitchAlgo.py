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

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
install()


sns.set() 

# add vehicles
truck1 = Vehicle('ego', model='car_mod_2', license='TRACTOR', color='Green')
truck2 = Vehicle('ego2', model='car_mod_2', license='TRACTOR2', color='Red')
trailer1 = Vehicle('trailer', model='boxutility_loaded_200')
trailer2 = Vehicle('trailer2', model='boxutility')
# trying to use function to make setup easier
truck1, truck2, trailer1, trailer2 = setup.initiateVehicles(truck1, truck2, trailer1, trailer2)

#manually connect the trailers and trucks in the beamNG game
time.sleep(10)


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
    """
    Determine the orientation of vector2 relative to vector1.
    
    Parameters:
        vector1 (numpy array): The first vector.
        vector2 (numpy array): The second vector.
        
    Returns:
        str: 'left' if vector2 is to the left of vector1,
             'right' if vector2 is to the right of vector1,
             'collinear' if the vectors are collinear.
    """
    # Compute the cross product
    cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]
    
    # Check the direction of the resulting vector
    if cross_product > 0:
        return 'left'
    elif cross_product < 0:
        return 'right'
    else:
        return 'collinear'


# set speed to 25m/s for testing sway

# truck1.ai_set_speed(25)
# truck2.ai_set_speed(25)

class ResettableTimer:
    def __init__(self, interval, callback):
        self.interval = interval
        self.callback = callback
        self.timer = None
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = True
        self.timer = threading.Timer(self.interval, self._callback_wrapper)
        self.timer.start()

    def _callback_wrapper(self):
        self.is_running = False
        self.callback()

    def start(self):
        if not self.is_running:
            self._run()

    def stop(self):
        if self.is_running:
            self.timer.cancel()
            self.is_running = False

    def reset(self):
        self.stop()
        self.start()
counter = 0
def left_on():
    global counter
    counter=0
    global truck1
    #truck1.set_color("Red")
    # truck1.set_lights(left_signal=True)   
def left_off():
    global counter
    counter=0
    global truck1
    #truck1.set_color("Orange")
    # truck1.set_lights(left_signal=False)   
def right_on():
    global counter
    counter=0
    global truck1
    #truck1.set_color("Green")
    # truck1.set_lights(right_signal=True)   
def right_off():
    global counter
    counter=0
    global truck1
    #truck1.set_color("Blue")
    # truck1.set_lights(right_signal=False)

# Create a Timer object that expires after 1 second
l_on = ResettableTimer(1, left_on)
l_off = ResettableTimer(2, left_off)
r_on = ResettableTimer(1, right_on)
r_off = ResettableTimer(2, right_off)

l_on.start()
l_off.start()
r_on.start()
r_off.start()


swerve_counter =0

while(swerve_counter < 400):
    poll_and_plot.pollVehicles(truck1, truck2, trailer1, trailer2)
    print(angle_between(truck1.state['dir'], trailer1.state['dir'] ))

    orientation_result = orientation(truck1.state['dir'], trailer1.state['dir'])
    print("Orientation:", orientation_result)
    """
    # truck1.set_velocity(5)
    # truck2.set_velocity(5)
    if(swerve_counter%8 == 0):
        test_sway.swerve_front(truck1, truck2, -1)
        left_count+=1
    elif(swerve_counter%4 == 0):
        test_sway.swerve_front(truck1, truck2, 1)
        right_count+=1
    else:
        test_sway.swerve_front(truck1, truck2, 0)    """

    swerve_counter+=1
    if angle_between(truck1.state['dir'], trailer1.state['dir'] ) > 3 and "right"== orientation(truck1.state['dir'], trailer1.state['dir']) :
        l_on.reset()
        l_off.reset()
    elif angle_between(truck1.state['dir'], trailer1.state['dir'] ) > 3 and "left"== orientation(truck1.state['dir'], trailer1.state['dir']):
        r_on.reset()
        r_off.reset()

    #elif angle_between(truck1.state['dir'], trailer1.state['dir'] ) > 10:
poll_and_plot.plot_poisitions(truck1, truck2, trailer1, trailer2)
l_on.stop()
l_off.stop()
r_on.stop()
r_off.stop()



#test_sway.moveHitchAndPoll(truck1, truck2, trailer1, trailer2)
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
