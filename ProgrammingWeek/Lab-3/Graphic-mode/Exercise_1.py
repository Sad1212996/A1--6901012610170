# Lab 3 - Graphic Ex 1
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# 1. ทดลองวาดรูปและสร้างแอนิเมชันโดยใช้ตัวอย่างจาก lecture slides และสังเกตผลที่ได้
# ลองทำลูกบอลวิ่งไปมาในจอ ถ้าชนขอบก็ให้เด้งกลับ (ใช้ if เช็คขอบ)

from processing import *

W = 400
H = 400

# ตำแหน่งและความเร็วของลูกบอล
x = 50
y = 200
speed_x = 4
speed_y = 3
size_ball = 40

def setup():
    size(W, H)
    frameRate(30)

def draw():
    global x, y, speed_x, speed_y
    background(230)

    # ขยับลูกบอลไปตามความเร็ว
    x = x + speed_x
    y = y + speed_y

    # ถ้าชนขอบซ้ายหรือขวา ให้กลับทิศแกน x
    if x > W - size_ball / 2 or x < size_ball / 2:
        speed_x = -speed_x

    # ถ้าชนขอบบนหรือล่าง ให้กลับทิศแกน y
    if y > H - size_ball / 2 or y < size_ball / 2:
        speed_y = -speed_y

    # ลองใช้ if-else เปลี่ยนสี ถ้าบอลอยู่ครึ่งซ้ายเป็นสีแดง ครึ่งขวาเป็นสีน้ำเงิน
    if x < W / 2:
        fill(255, 80, 80)
    else:
        fill(80, 80, 255)

    ellipse(x, y, size_ball, size_ball)

    # สังเกต: ถ้าไม่ใส่ background() ทุกเฟรม ลูกบอลจะทิ้งรอยเป็นเส้นยาว

run()
