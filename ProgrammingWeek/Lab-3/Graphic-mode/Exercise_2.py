# Lab 3 - Graphic Ex 2
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# 2. สร้างฟังก์ชันสำหรับวาดรูปสี่เหลี่ยมจัตุรัส draw_square()
# และนำไปใช้สร้างรูปเครื่องหมายบวก ใน draw_positive()
# เพิ่ม Animation และ Interaction เช่น เปลี่ยนตำแหน่ง หรือ ขนาด
# และมีการนำคำสั่งทางเลือกมาใช้ซ้อนกัน (nested)

from processing import *

W = 400
H = 400

# ตำแหน่งกลางของเครื่องหมายบวก และขนาดของสี่เหลี่ยม 1 ช่อง
px = 200
py = 200
s = 30
speed = 3

def setup():
    size(W, H)
    frameRate(30)

def draw_square(x, y, side):
    # วาดสี่เหลี่ยมจัตุรัส โดยให้ (x, y) เป็นจุดกึ่งกลาง
    rect(x - side / 2, y - side / 2, side, side)

def draw_positive(x, y, side):
    # เครื่องหมายบวก = สี่เหลี่ยม 5 ช่อง (ตรงกลาง บน ล่าง ซ้าย ขวา)
    draw_square(x, y, side)          # กลาง
    draw_square(x, y - side, side)   # บน
    draw_square(x, y + side, side)   # ล่าง
    draw_square(x - side, y, side)   # ซ้าย
    draw_square(x + side, y, side)   # ขวา

def draw():
    global px, py, s, speed
    background(240)

    # Animation: ให้เครื่องหมายบวกเลื่อนไปทางขวาเรื่อยๆ ชนขอบแล้วเด้งกลับ
    px = px + speed
    if px > W - s * 1.5 or px < s * 1.5:
        speed = -speed

    # Interaction: ถ้ากดเมาส์ค้างไว้ จะขยายขนาด
    # nested if: เช็คก่อนว่ากดเมาส์ไหม แล้วค่อยเช็คว่าขนาดเกินแล้วหรือยัง
    if mouse.pressed:
        if s < 60:
            s = s + 1
        else:
            s = 20   # ใหญ่สุดแล้ว ให้กลับไปเล็กใหม่
        # ตามเมาส์ในแนวตั้งตอนกดด้วย
        py = mouse.y

    # เปลี่ยนสีตามตำแหน่ง โดยใช้ if ซ้อน if แบ่งจอเป็น 4 ส่วน
    if px < W / 2:
        if py < H / 2:
            fill(255, 100, 100)   # ซ้ายบน แดง
        else:
            fill(100, 200, 100)   # ซ้ายล่าง เขียว
    else:
        if py < H / 2:
            fill(100, 100, 255)   # ขวาบน น้ำเงิน
        else:
            fill(255, 200, 50)    # ขวาล่าง เหลือง

    draw_positive(px, py, s)

run()
