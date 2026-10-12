# ==========================================
# Lab 10 - Counter App (โปรแกรมนับจำนวนตัวเลข)
# ผู้เขียน: นายพชรพล ชนะศรี  L2  6901012610170
# ==========================================

import tkinter as tk

# ตัวแปรเก็บค่าตัวเลขปัจจุบัน เริ่มต้นที่ 0
count = 0


def update_label():
    # เอาค่า count ไปแสดงบน Label
    label_count.config(text=str(count))


def increase():
    # กดปุ่ม Increase -> เพิ่มค่าทีละ 1
    global count  # ต้องใส่ global เพราะจะแก้ค่าตัวแปรที่อยู่นอกฟังก์ชัน
    count += 1
    update_label()


def decrease():
    # กดปุ่ม Decrease -> ลดค่าทีละ 1
    global count
    count -= 1
    update_label()


def reset():
    # กดปุ่ม Reset -> ตั้งค่ากลับเป็น 0
    global count
    count = 0
    update_label()


# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("Counter App - พชรพล ชนะศรี")
window.geometry("300x200")

# Label แสดงตัวเลข ตั้งฟอนต์ใหญ่ๆ ให้อ่านง่าย
label_count = tk.Label(window, text="0", font=("Arial", 40))
label_count.pack(pady=10)

# ทำ Frame ไว้ใส่ปุ่ม จะได้วางปุ่มเรียงกันแนวนอน
frame_btn = tk.Frame(window)
frame_btn.pack()

# ปุ่มทั้ง 3 ปุ่ม ผูกฟังก์ชันด้วย command= (ใส่แค่ชื่อฟังก์ชัน ไม่ต้องมีวงเล็บ)
btn_inc = tk.Button(frame_btn, text="Increase", width=8, command=increase)
btn_inc.grid(row=0, column=0, padx=5)

btn_dec = tk.Button(frame_btn, text="Decrease", width=8, command=decrease)
btn_dec.grid(row=0, column=1, padx=5)

btn_reset = tk.Button(frame_btn, text="Reset", width=8, command=reset)
btn_reset.grid(row=0, column=2, padx=5)

# วนรอรับ Event จากผู้ใช้ (ถ้าไม่ใส่ หน้าต่างจะเปิดแล้วปิดทันที)
window.mainloop()

# ------------------------------------------
# Error ที่เจอระหว่างทำ (พร้อมวิธีแก้)
# 1. UnboundLocalError: local variable 'count' referenced before assignment
#    -> ลืมใส่ global count ในฟังก์ชัน แก้โดยเพิ่ม global count
# 2. กดปุ่มไม่ได้ แต่ตัวเลขเปลี่ยนตอนเปิดโปรแกรมครั้งเดียว
#    -> เขียน command=increase() มีวงเล็บ ทำให้ฟังก์ชันถูกเรียกทันที
#       แก้เป็น command=increase
# ------------------------------------------
