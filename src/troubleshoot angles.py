import numpy as np
import math
 
from math import atan2, degrees

def sudut(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

print(sudut([5.1, 3.5], [4.3, 3. ], [5.8, 4. ], ))

a = np.array([6.3, 3.3])
b = np.array([4.9, 2.5])
c = np.array([7.9, 3.8])

ba = a - b
bc = c - b

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle = np.arccos(cosine_angle)

print(np.degrees(angle))