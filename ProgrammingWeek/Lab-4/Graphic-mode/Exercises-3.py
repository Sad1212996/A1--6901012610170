# Lab 4 - Graphic Ex 3 (Interactive Robot/Face)
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

from math import sin
from processing import *

def draw_eye(x, y, r):
    # Subroutine วาดตาด้วย ellipse
    ellipse(x, y, r, r)
    ellipse(x, y, r / 3, r / 3)

def draw_antenna(x, y):
    # Subroutine วาดเสาอากาศด้วย line และ ellipse
    line(x, y, x, y - 40)
    ellipse(x, y - 40, 15, 15)

def draw_mouth(x, y):
    # Subroutine วาดปากแบบเส้นตะแกรงโดยใช้ loop และ line
    line(x - 30, y, x + 30, y)
    i = -30
    while i <= 30:
        line(x + i, y - 5, x + i, y + 5)
        i = i + 10 # ระยะห่างของเส้นซี่ฟัน

def draw_robot(x, y):
    # รวม Subroutines วาดหุ่นยนต์
    draw_antenna(x, y - 60)
    ellipse(x, y, 140, 120) # หัว
    draw_eye(x - 30, y - 10, 30) # ตาซ้าย
    draw_eye(x + 30, y - 10, 30) # ตาขวา
    draw_mouth(x, y + 30) # ปาก

def setup():
    size(500, 500)

def draw():
    background(200, 220, 255)
    # ติดตามตำแหน่งเมาส์ Interaction
    draw_robot(mouseX, mouseY)

run()