# Lab 5 - Graphic 
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

from math import sin, sqrt
from processing import *

NORMAL_EXTENT = 50    # ขนาดปกติของสี่เหลี่ยมแต่ละแท่งในเครื่องหมายบวก (เท่ากับของเดิม)
HOVER_EXTENT = 70     # ขนาดตอนเมาส์เข้าใกล้ (ทำให้รูปดูขยายใหญ่ขึ้น)
HOVER_DIST = 90       # ระยะที่ถือว่า "ใกล้" เมาส์ (หน่วยพิกเซล)


def square(x, y, extent):
    # ใช้ rect แทน square เพื่อป้องกัน NameError ในระบบ Processing Python Mode
    rect(x, y, extent, extent)


def draw_positive(x, y, extent):
    # วาดรูปเครื่องหมายบวกจากสี่เหลี่ยม 5 รูป (เหมือนเดิม)
    # เพิ่มพารามิเตอร์ extent เข้ามา เพื่อให้ปรับขนาดได้ตอนมีปฏิสัมพันธ์กับเมาส์
    # ระยะห่างระหว่างแท่ง (offset) ใช้ค่าเท่ากับ extent เสมอ
    # เพื่อให้สี่เหลี่ยมชนกันพอดีเป็นรูปกากบาท ไม่มีช่องว่างหรือซ้อนทับ (เหมือนตอน extent = 50 ในโค้ดเดิม)
    square(x, y + extent, extent)                  # แท่งซ้าย
    square(x + extent * 2, y + extent, extent)      # แท่งขวา
    square(x + extent, y + extent, extent)          # แท่งกลาง
    square(x + extent, y, extent)                   # แท่งบน
    square(x + extent, y + extent * 2, extent)       # แท่งล่าง


def dist2(x1, y1, x2, y2):
    # ไลบรารีนี้ไม่มี dist() ให้ใช้เหมือน Processing ทั่วไป จึงคำนวณระยะทางเอง
    # ด้วยทฤษฎีพีทาโกรัส: ระยะทาง = sqrt( (x1-x2)^2 + (y1-y2)^2 )
    dx = x1 - x2
    dy = y1 - y2
    return sqrt(dx * dx + dy * dy)


def setup():
    size(600, 400)


def draw():
    background(240)

    fc = environment.frameCount   # จำนวนเฟรมที่ผ่านมา ใช้เป็นตัวแปรเวลาสำหรับคลื่น sine (Animation)

    # ใช้ while loop เพื่อวาด draw_positive เรียงต่อกันแนวนอน (เหมือนเดิม)
    x_pos = 20
    i = 0                          # ตัวนับลำดับของแต่ละรูป ใช้เลื่อนเฟสให้ไม่ขึ้นลงพร้อมกัน
    while x_pos < width:
        # ---------- Animation: ให้แต่ละรูปลอยขึ้น-ลงตามคลื่น sine ----------
        y_offset = sin(fc / 10.0 + i) * 15   # แกว่งขึ้นลง +/- 15 พิกเซล คนละจังหวะกัน
        y_pos = 100 + y_offset

        # ---------- Interaction: ขยายขนาดเมื่อเมาส์เข้าใกล้รูปนี้ ----------
        center_x = x_pos + NORMAL_EXTENT     # ตำแหน่งกึ่งกลางโดยประมาณของรูปเครื่องหมายบวก
        center_y = y_pos + NORMAL_EXTENT
        d = dist2(mouse.x, mouse.y, center_x, center_y)
        if d < HOVER_DIST:
            extent = HOVER_EXTENT
        else:
            extent = NORMAL_EXTENT

        draw_positive(x_pos, y_pos, extent)

        x_pos = x_pos + 180        # ขยับตำแหน่ง x ไปทางขวาในแต่ละรอบ (เหมือนเดิม)
        i = i + 1


run()