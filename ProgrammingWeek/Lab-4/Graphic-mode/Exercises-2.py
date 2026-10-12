# Lab 4 - Graphic Ex 2
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

from math import sin
from processing import *

def square(x, y, extent):
    # ใช้ rect แทน square เพื่อป้องกัน NameError ในระบบ Processing Python Mode
    rect(x, y, extent, extent)

def draw_positive(x, y):
    # วาดรูปเครื่องหมายบวกจากสี่เหลี่ยม 5 รูป
    square(x, y + 50, 50)
    square(x + 100, y + 50, 50)
    square(x + 50, y + 50, 50)
    square(x + 50, y, 50)
    square(x + 50, y + 100, 50)

def setup():
    size(600, 400)

def draw():
    background(240)
    
    # ใช้ while loop เพื่อวาด draw_positive เรียงต่อกันแนวแนวนอน
    x_pos = 20
    while x_pos < width:
        draw_positive(x_pos, 100)
        x_pos = x_pos + 180 # ขยับตำแหน่ง x ไปทางขวาในแต่ละรอบ

run()