# Lab 4 - Graphic Ex 1
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

from math import sin
from processing import *

def setup():
    size(400, 400)
    frameRate(10) # กำหนดอัตราเฟรม 10 เฟรมต่อวินาที

def draw_rain_drops(n):
    # วาดวงกลมสุ่มตำแหน่งและขนาดจำนวน n วง โดยใช้ while loop[cite: 2]
    i = 0
    while i < n:
        x = random(50, 350)
        y = random(50, 350)
        r = random(10, 40)
        ellipse(x, y, r, r) # วาดวงกลม
        i = i + 1

def draw():
    background(220) # ล้างหน้าจอทุกเฟรม[cite: 2]
    draw_rain_drops(5) # วาดหยดน้ำสุ่ม 5 จุดทุกเฟรม

run()