# Lab 3 - Graphic Ex 3
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# 3. สร้าง Animation และ Interaction จากการวาดรูปสิ่งที่ชอบ
# ใช้ได้แค่ line() กับ ellipse() และแบ่งงานเป็นฟังก์ชันย่อย (subroutine)
# ผมเลือกวาดแมว draw_cat() แบ่งเป็น draw_tail(), draw_body(), draw_head(),
# draw_ears(), draw_eyes(), draw_nose(), draw_whiskers()

from math import sin
from processing import *

W = 400
H = 400

cat_x = 200      # ตำแหน่งแมวแนวนอน
cat_y = 260      # ตำแหน่งแมวแนวตั้ง (ใช้ตอนกระโดด)
jump_v = 0       # ความเร็วตอนกระโดด
t = 0            # ตัวนับเฟรม เอาไว้ใช้ทำแอนิเมชัน

def setup():
    size(W, H)
    frameRate(30)

def draw_tail(x, y):
    # หางแกว่งไปมาโดยใช้ sin
    swing = sin(t * 0.2) * 25
    line(x + 40, y + 20, x + 80, y - 20 + swing)

def draw_body(x, y):
    ellipse(x, y + 30, 100, 70)

def draw_head(x, y):
    ellipse(x, y - 30, 80, 70)

def draw_ears(x, y):
    # หูเป็นสามเหลี่ยม วาดด้วย line 3 เส้นต่อหู
    line(x - 35, y - 45, x - 25, y - 80)
    line(x - 25, y - 80, x - 10, y - 60)
    line(x + 35, y - 45, x + 25, y - 80)
    line(x + 25, y - 80, x + 10, y - 60)

def draw_eyes(x, y):
    # กระพริบตาทุกๆ 60 เฟรม (ตาปิดประมาณ 5 เฟรม)
    if t % 60 < 5:
        line(x - 22, y - 35, x - 8, y - 35)
        line(x + 8, y - 35, x + 22, y - 35)
    else:
        fill(0)
        ellipse(x - 15, y - 35, 10, 14)
        ellipse(x + 15, y - 35, 10, 14)
        fill(255, 200, 120)   # กลับเป็นสีตัวแมว

def draw_nose(x, y):
    ellipse(x, y - 22, 6, 4)

def draw_whiskers(x, y):
    line(x - 10, y - 20, x - 45, y - 25)
    line(x - 10, y - 18, x - 45, y - 15)
    line(x + 10, y - 20, x + 45, y - 25)
    line(x + 10, y - 18, x + 45, y - 15)

def draw_cat(x, y):
    fill(255, 200, 120)
    draw_tail(x, y)
    draw_body(x, y)
    draw_head(x, y)
    draw_ears(x, y)
    draw_eyes(x, y)
    draw_nose(x, y)
    draw_whiskers(x, y)

def draw():
    global cat_x, cat_y, jump_v, t
    background(200, 230, 255)
    t = t + 1

    # พื้น
    line(0, 320, W, 320)

    # Animation + Interaction: แมวเดินตามเมาส์ในแนวนอน
    if mouse.x > cat_x + 5:
        cat_x = cat_x + 2
    elif mouse.x < cat_x - 5:
        cat_x = cat_x - 2

    # คลิกเมาส์ให้แมวกระโดด แต่ต้องยืนอยู่บนพื้นก่อน (ไม่งั้นกระโดดกลางอากาศได้)
    if mouse.pressed:
        if cat_y >= 260:
            jump_v = -12

    # แรงโน้มถ่วงดึงแมวลง
    cat_y = cat_y + jump_v
    if cat_y < 260:
        jump_v = jump_v + 1
    else:
        cat_y = 260
        jump_v = 0

    draw_cat(cat_x, cat_y)

run()
