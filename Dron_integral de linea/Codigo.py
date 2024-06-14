
from djitellopy import Tello
import sympy as sp 
import math 
import numpy as np
import time 

alturas = []

tello = Tello()
tello.connect()
tello.streamoff()

print('Bateria',tello.get_battery())


tello.takeoff()
#Coordenadas
h = tello.get_height()
#print(h)
alturas.append(h)

x=[125,125,125,125]
y=[]
z=[100,-100,100,-100]
area = 0
s = [] #surface


for i in range(4):

    tello.go_xyz_speed(x[i],0,z[i],90)
    #time.sleep(1)
    h = tello.get_height()
    #print(h)
    alturas.append(h)
    area += ( alturas[-1] + alturas[-2]) *125 / 2 
    print(area)  
    s.append(area)

tello.rotate_counter_clockwise(90)
tello.move_forward(100)
#time.sleep(1)
h = tello.get_height()
alturas.append(h)
area += alturas[-1] * 100
s.append(area)
print(area)

tello.rotate_counter_clockwise(90)

for i in range(4):
    tello.go_xyz_speed(x[i],0,z[i],100)
    #time.sleep(1)
    h = tello.get_height()
    #print(h)
    alturas.append(h)
    area += ( alturas[-1] + alturas[-2]) *125 / 2   
    s.append(area)
    print(area)

tello.rotate_counter_clockwise(90)
tello.move_forward(100)
h = tello.get_height()
alturas.append(h)
area += alturas[-1] * 100
s.append(area)
print(area)

tello.rotate_counter_clockwise(90)
tello.land()

print(alturas)
print(s)
print(s[-1])
print(area)



