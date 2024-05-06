import math
import numpy as np
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
"""
import pickle

aba = ["a", "b", "a"]
with open('outfile', 'wb') as fp:
    pickle.dump(aaa, fp)
with open ('outfile', 'rb') as fp:
    itemlist = pickle.load(fp)
print(itemlist[1])
"""