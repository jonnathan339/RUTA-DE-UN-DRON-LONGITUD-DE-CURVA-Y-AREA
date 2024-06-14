from djitellopy import Tello
import sympy as sp 
import math 
import numpy as np
import time 

tello = Tello()

tello.connect()

tello.streamoff()

print('Bateria',tello.get_battery())


tello.takeoff()
time.sleep(2)
#Coordenadas
    
print(tello.get_height())

#tello.go_xyz_speed(25,0,70,100)
tello.send_rc_control(0,25,50,0)
time.sleep(2)
#tello.send_rc_control(0,0,0,0)
#time.sleep(2)

print(tello.get_height())

tello.send_rc_control(0,25,-50,0)
#tello.go_xyz_speed(25,0,-80,100)
time.sleep(2)
#tello.send_rc_control(0,0,0,0)
print(tello.get_height())

#tello.go_xyz_speed(25,0,70,100)
tello.send_rc_control(0,25,50,0)
#tello.send_rc_control(0,0,0,0)
time.sleep(1)
print(tello.get_height())


tello.send_rc_control(0,25,-50,0)
#tello.send_rc_control(0,0,0,0)
#tello.go_xyz_speed(25,0,-80,100)
time.sleep(1)
print(tello.get_height())


tello.land()
"""




tello.go_xyz_speed(100,0,0,100)

time.sleep(2)
print(tello.get_height())

tello.rotate_counter_clockwise(90)



#tello.send_rc_control(0,0,0,0)
time.sleep(1)
tello.land()


"""
