# ==========================================
# Lab 10 - Celsius to Fahrenheit Converter (โปรแกรมแปลงอุณหภูมิ)
# ผู้เขียน: นายพชรพล ชนะศรี  L2  6901012610170
# ==========================================

import tkinter as tk


def convert():
    # ดึงข้อความที่ผู้ใช้กรอกจากช่อง Entry ด้วย get()
    text = entry_c.get()

    try:
        # แปลงเป็น float ก่อน ถ้าพิมพ์ไม่ใช่ตัวเลขจะเด้งไป except
        c = float(text)
        f = c * 9 / 5 + 32  # สูตร F = C x 9/5 + 32
        label_result.config(text=f"{c} °C = {f:.2f} °F", fg="black")
    except ValueError:
        # กรณีกรอกตัวอักษร หรือปล่อยว่าง ให้แจ้งเตือนเป็นสีแดง
        label_result.config(text="กรุณากรอกตัวเลขเท่านั้น!", fg="red")


# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("C to F Converter - พชรพล ชนะศรี")
window.geometry("320x160")

# ใช้ grid จัดเป็นแถว/คอลัมน์ บรรทัดแรก: ข้อความ + ช่องกรอก
tk.Label(window, text="องศาเซลเซียส (°C):").grid(row=0, column=0, padx=10, pady=10)

entry_c = tk.Entry(window, width=12)
entry_c.grid(row=0, column=1, pady=10)

# ปุ่ม Convert ผูกกับฟังก์ชัน convert
btn_convert = tk.Button(window, text="Convert", command=convert)
btn_convert.grid(row=1, column=0, columnspan=2, pady=5)

# Label ไว้โชว์ผลลัพธ์ (ตอนแรกยังว่าง)
label_result = tk.Label(window, text="", font=("Arial", 12))
label_result.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()

# ------------------------------------------
# Error ที่เจอระหว่างทำ (พร้อมวิธีแก้)
# 1. ValueError: could not convert string to float: 'abc'
#    -> ผู้ใช้กรอกตัวหนังสือ แก้โดยครอบด้วย try/except ValueError
# 2. TypeError: can't multiply sequence by non-int of type 'float'
#    -> ลืมแปลงค่าจาก get() ซึ่งเป็น string ก่อนคำนวณ แก้โดยใช้ float()
# 3. AttributeError: 'NoneType' object has no attribute 'get'
#    -> เขียน entry_c = tk.Entry(...).grid(...) ในบรรทัดเดียว
#       grid() คืนค่า None เลยต้องแยก grid() ไว้อีกบรรทัด
# ------------------------------------------
