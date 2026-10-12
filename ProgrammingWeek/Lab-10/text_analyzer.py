# ==========================================
# Lab 10 - GUI Text Analyzer (โปรแกรมวิเคราะห์ข้อความ)
# ผู้เขียน: นายพชรพล ชนะศรี  L2  6901012610170
# ==========================================

import tkinter as tk


def count_character():
    # นับว่าตัวอักษรที่ระบุ มีอยู่ในข้อความกี่ตัว
    text = entry_text.get()
    char = entry_char.get()

    # เช็คก่อนว่าผู้ใช้กรอกตัวอักษรมาแค่ 1 ตัวไหม
    if len(char) != 1:
        label_result.config(text="กรุณากรอกตัวอักษรค้นหา 1 ตัว", fg="red")
        return

    # ใช้ lower() ทั้งคู่ จะได้นับไม่สนตัวพิมพ์เล็ก/ใหญ่ แล้วใช้ count() ของ string
    n = text.lower().count(char.lower())
    label_result.config(text=f"ตัวอักษร '{char}' มีทั้งหมด {n} ตัว", fg="black")


def count_vowels():
    # นับสระ a e i o u ทั้งหมดในข้อความ
    text = entry_text.get().lower()
    vowels = "aeiou"
    n = 0
    for ch in text:
        if ch in vowels:
            n += 1
    label_result.config(text=f"มีสระทั้งหมด {n} ตัว", fg="black")


def check_palindrome():
    # Palindrome = อ่านจากหน้าไปหลัง กับหลังไปหน้าได้เหมือนกัน เช่น "level"
    text = entry_text.get()

    # ตัดช่องว่างออกแล้วทำเป็นตัวเล็กหมด เผื่อพิมพ์ "Never odd or even"
    clean = text.replace(" ", "").lower()

    if clean == "":
        label_result.config(text="กรุณาพิมพ์ข้อความก่อน", fg="red")
    elif clean == clean[::-1]:  # [::-1] คือกลับด้าน string
        label_result.config(text=f"'{text}' เป็น Palindrome", fg="green")
    else:
        label_result.config(text=f"'{text}' ไม่เป็น Palindrome", fg="black")


# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("Text Analyzer - พชรพล ชนะศรี")
window.geometry("420x230")

# แถว 0: ช่องพิมพ์ข้อความ
tk.Label(window, text="ข้อความ:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
entry_text = tk.Entry(window, width=30)
entry_text.grid(row=0, column=1, columnspan=2, pady=8, sticky="w")

# แถว 1: ช่องตัวอักษรที่ต้องการค้นหา (ทำให้สั้นๆ)
tk.Label(window, text="ตัวอักษรค้นหา:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
entry_char = tk.Entry(window, width=5)
entry_char.grid(row=1, column=1, pady=8, sticky="w")

# แถว 2: ปุ่ม 3 ปุ่มเรียงกัน
btn_char = tk.Button(window, text="Count Character", command=count_character)
btn_char.grid(row=2, column=0, padx=5, pady=10)

btn_vowel = tk.Button(window, text="Count Vowels", command=count_vowels)
btn_vowel.grid(row=2, column=1, padx=5, pady=10)

btn_pal = tk.Button(window, text="Check Palindrome", command=check_palindrome)
btn_pal.grid(row=2, column=2, padx=5, pady=10)

# แถว 3: Label แสดงผลลัพธ์
label_result = tk.Label(window, text="ผลลัพธ์จะแสดงตรงนี้", font=("Arial", 12))
label_result.grid(row=3, column=0, columnspan=3, pady=10)

window.mainloop()

# ------------------------------------------
# Error ที่เจอระหว่างทำ (พร้อมวิธีแก้)
# 1. TclError: cannot use geometry manager pack inside . which already has slaves managed by grid
#    -> ใช้ pack() กับ grid() ปนกันในหน้าต่างเดียว แก้โดยใช้ grid() อย่างเดียว
# 2. นับ "Bangkok" หาตัว "B" ได้ 0 ตัว ทั้งที่มี
#    -> ไม่ได้แปลงเป็นตัวเล็กทั้งคู่ แก้โดยใช้ lower() ทั้งข้อความและตัวอักษร
# 3. NameError: name 'entry_text' is not defined
#    -> พิมพ์ชื่อตัวแปรผิด (เช่น entry_txt) แก้ให้ชื่อตรงกัน
# ------------------------------------------
