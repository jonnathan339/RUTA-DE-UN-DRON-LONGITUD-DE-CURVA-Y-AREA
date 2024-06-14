from djitellopy import Tello
import sympy as sp 
import math 
import numpy as np
import time 

tello = Tello()

tello.connect()

tello.streamoff()

print('Bateria',tello.get_battery())

print(tello.get_height())

print(tello.get_height())


print(tello.get_acceleration_x())




