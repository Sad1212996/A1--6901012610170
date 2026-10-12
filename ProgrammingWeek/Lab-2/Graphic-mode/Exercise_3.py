from math import sin
from processing import *

y = 0 

def setup():
    size(400, 350)
    
def draw():
    global y
    draw_balloon(200, y) 
    
    y = y + 5 
    
    if y > 350: 
        y = -100 
    
def draw_balloon(x, y):
    ellipse(x, y, 100, 100)
    line(x, y + 50, x, y + 200)

run()

# Lab 2: Function :L2
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170
