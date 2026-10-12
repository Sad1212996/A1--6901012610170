"""
ไฟล์เรียนรู้ tkinter (GUI พื้นฐานของ Python)
รันไฟล์นี้แล้วดูหน้าต่าง GUI ที่เปิดขึ้นมา
แต่ละส่วนมีคอมเมนต์อธิบายคำสั่งและผลลัพธ์ที่ได้
"""

import tkinter as tk
from tkinter import ttk          # ttk = ธีมสวยกว่า widget ปกติของ tkinter
from tkinter import messagebox   # กล่องข้อความ popup (แจ้งเตือน/ถาม/error)


# ---------------------------------------------------------
# 1) สร้างหน้าต่างหลัก (Root Window)
# ---------------------------------------------------------
root = tk.Tk()                       # สร้างหน้าต่างหลัก ต้องมีเสมอ 1 อันต่อโปรแกรม
root.title("เรียนรู้ tkinter")        # ตั้งชื่อ title bar
root.geometry("500x600")             # ขนาดหน้าต่าง กว้างxสูง (พิกเซล)
root.configure(bg="#f0f0f0")         # สีพื้นหลังหน้าต่าง
# root.resizable(False, False)       # ปิดการปรับขนาด (แกน x, แกน y)


# ---------------------------------------------------------
# 2) Label = ป้ายข้อความ แสดงข้อความอย่างเดียว แก้ไขไม่ได้
# ---------------------------------------------------------
label_title = tk.Label(
    root,
    text="ตัวอย่างคำสั่ง tkinter ที่ใช้บ่อย",
    font=("TH Sarabun New", 16, "bold"),
    fg="blue",       # สีตัวอักษร (foreground)
    bg="#f0f0f0",    # สีพื้นหลัง
)
label_title.pack(pady=10)  # pack() = วาง widget แบบเรียงต่อกัน, pady = ระยะห่างแนวตั้ง


# ---------------------------------------------------------
# 3) Entry = ช่องกรอกข้อความบรรทัดเดียว
# ---------------------------------------------------------
label_name = tk.Label(root, text="กรอกชื่อ:", bg="#f0f0f0")
label_name.pack()

entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)
entry_name.insert(0, "")  # insert(index, text) = ใส่ข้อความเริ่มต้นในช่อง


def show_name():
    """อ่านค่าจาก Entry แล้วโชว์ popup"""
    name = entry_name.get()  # get() = ดึงข้อความที่พิมพ์ในช่อง
    if name == "":
        messagebox.showwarning("แจ้งเตือน", "กรุณากรอกชื่อก่อน")
    else:
        messagebox.showinfo("ผลลัพธ์", f"สวัสดี, {name}!")


# ---------------------------------------------------------
# 4) Button = ปุ่มกด เรียกฟังก์ชันเมื่อคลิก
# ---------------------------------------------------------
btn_show = tk.Button(
    root,
    text="แสดงชื่อ",
    command=show_name,   # command = ฟังก์ชันที่ทำงานเมื่อคลิกปุ่ม (ห้ามใส่วงเล็บ)
    bg="#4CAF50",
    fg="white",
)
btn_show.pack(pady=5)


# ---------------------------------------------------------
# 5) Checkbutton = ช่องกาถูก (เลือกได้/ไม่เลือก)
# ---------------------------------------------------------
check_var = tk.BooleanVar()  # ตัวแปรพิเศษของ tkinter สำหรับเก็บค่า True/False

check_agree = tk.Checkbutton(
    root,
    text="ฉันยอมรับเงื่อนไข",
    variable=check_var,   # ผูกกับตัวแปรด้านบน
    bg="#f0f0f0",
)
check_agree.pack(pady=5)


# ---------------------------------------------------------
# 6) Radiobutton = ปุ่มตัวเลือกแบบเลือกได้ข้อเดียว
# ---------------------------------------------------------
radio_var = tk.StringVar(value="ชาย")  # ตัวแปรเก็บค่าที่เลือก เริ่มต้น = "ชาย"

frame_radio = tk.Frame(root, bg="#f0f0f0")  # Frame = กล่องจัดกลุ่ม widget
frame_radio.pack(pady=5)

tk.Radiobutton(frame_radio, text="ชาย", variable=radio_var, value="ชาย", bg="#f0f0f0").pack(side="left")
tk.Radiobutton(frame_radio, text="หญิง", variable=radio_var, value="หญิง", bg="#f0f0f0").pack(side="left")
# side="left" = วางเรียงจากซ้ายไปขวาแทนที่จะเรียงบนลงล่าง


# ---------------------------------------------------------
# 7) Listbox = กล่องแสดงรายการให้เลือก (เลือกได้หลายบรรทัด)
# ---------------------------------------------------------
listbox = tk.Listbox(root, height=4)
listbox.pack(pady=5)

for item in ["แอปเปิล", "กล้วย", "มะม่วง", "สับปะรด"]:
    listbox.insert(tk.END, item)  # tk.END = แทรกต่อท้ายรายการ


def show_selected():
    """แสดงรายการที่เลือกใน Listbox"""
    selection = listbox.curselection()  # curselection() = คืน index ที่เลือก (tuple)
    if selection:
        value = listbox.get(selection[0])  # get(index) = ดึงข้อความจาก index
        messagebox.showinfo("เลือกแล้ว", f"คุณเลือก: {value}")


tk.Button(root, text="ดูรายการที่เลือก", command=show_selected).pack(pady=5)


# ---------------------------------------------------------
# 8) Combobox (จาก ttk) = dropdown ให้เลือกค่า
# ---------------------------------------------------------
combo_var = tk.StringVar()

combo = ttk.Combobox(
    root,
    textvariable=combo_var,
    values=["กรุงเทพ", "เชียงใหม่", "ภูเก็ต", "ขอนแก่น"],
    state="readonly",  # readonly = เลือกได้จากลิสต์เท่านั้น พิมพ์เองไม่ได้
)
combo.current(0)  # current(index) = เลือกค่าเริ่มต้นตาม index
combo.pack(pady=5)


# ---------------------------------------------------------
# 9) Scale = แถบเลื่อนปรับค่าตัวเลข
# ---------------------------------------------------------
scale_var = tk.IntVar()

scale = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",  # horizontal = แนวนอน, vertical = แนวตั้ง
    variable=scale_var,
    bg="#f0f0f0",
)
scale.pack(pady=5)


# ---------------------------------------------------------
# 10) Text = กล่องข้อความหลายบรรทัด (ต่างจาก Entry ที่มีบรรทัดเดียว)
# ---------------------------------------------------------
text_box = tk.Text(root, height=4, width=40)
text_box.pack(pady=5)
text_box.insert("1.0", "พิมพ์ข้อความหลายบรรทัดที่นี่...")  # "1.0" = บรรทัด 1 ตำแหน่ง 0


# ---------------------------------------------------------
# 11) Frame + grid layout = อีกวิธีจัดวาง widget (แถว/คอลัมน์)
# ---------------------------------------------------------
frame_grid = tk.Frame(root, bg="#f0f0f0")
frame_grid.pack(pady=10)

tk.Label(frame_grid, text="แถว0 คอลัมน์0", bg="lightblue").grid(row=0, column=0, padx=3, pady=3)
tk.Label(frame_grid, text="แถว0 คอลัมน์1", bg="lightgreen").grid(row=0, column=1, padx=3, pady=3)
tk.Label(frame_grid, text="แถว1 คอลัมน์0", bg="lightyellow").grid(row=1, column=0, padx=3, pady=3)
tk.Label(frame_grid, text="แถว1 คอลัมน์1", bg="lightpink").grid(row=1, column=1, padx=3, pady=3)
# grid(row=, column=) = จัดวางแบบตาราง ห้ามผสมกับ pack() ใน widget ระดับเดียวกัน


# ---------------------------------------------------------
# 12) place = จัดวางตามพิกัด x, y แน่นอน (ใช้น้อย ควบคุมยาก)
# ---------------------------------------------------------
# tk.Label(root, text="ตำแหน่งคงที่").place(x=10, y=10)


# ---------------------------------------------------------
# 13) เมนูบาร์ (Menu)
# ---------------------------------------------------------
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)  # tearoff=0 = ปิดเส้นประดึงเมนูออกมาลอย
file_menu.add_command(label="ใหม่", command=lambda: print("คลิกเมนูใหม่"))
file_menu.add_command(label="เปิด", command=lambda: print("คลิกเมนูเปิด"))
file_menu.add_separator()  # เส้นคั่นเมนู
file_menu.add_command(label="ออก", command=root.quit)  # root.quit() = ปิดโปรแกรม

menu_bar.add_cascade(label="ไฟล์", menu=file_menu)


# ---------------------------------------------------------
# 14) ปุ่มปิดโปรแกรม
# ---------------------------------------------------------
def on_exit():
    """ยืนยันก่อนปิดโปรแกรม"""
    if messagebox.askyesno("ยืนยัน", "ต้องการปิดโปรแกรมหรือไม่?"):
        root.destroy()  # destroy() = ปิดหน้าต่างทันที (ต่างจาก quit ที่แค่หยุด mainloop)


tk.Button(root, text="ปิดโปรแกรม", command=on_exit, bg="#f44336", fg="white").pack(pady=10)


# ---------------------------------------------------------
# 15) mainloop() = เริ่มลูปรอรับ event (คลิก/พิมพ์ ฯลฯ)
#     ต้องอยู่บรรทัดสุดท้ายเสมอ ไม่งั้นหน้าต่างจะเปิดแล้วปิดทันที
# ---------------------------------------------------------
root.mainloop()
