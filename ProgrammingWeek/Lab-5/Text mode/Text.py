# Lab 5 - Text mode 
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

# ---------- a. หาค่า max / min / average ของอะเรย์ ----------

def find_max(a):
    # สมมติว่าค่าแรกในอะเรย์เป็นค่ามากที่สุดไว้ก่อน
    max_val = a[0]
    i = 1  # เริ่มเทียบจากตัวที่ 2 (index 1) เพราะตัวแรกถูกใช้เป็นค่าเริ่มต้นแล้ว
    while i < len(a):
        if a[i] > max_val:      # ถ้าค่าปัจจุบันมากกว่าค่าที่จำไว้
            max_val = a[i]      # อัปเดตค่ามากที่สุด
        i = i + 1
    return max_val


def find_min(a):
    # สมมติว่าค่าแรกในอะเรย์เป็นค่าน้อยที่สุดไว้ก่อน
    min_val = a[0]
    i = 1
    while i < len(a):
        if a[i] < min_val:      # ถ้าค่าปัจจุบันน้อยกว่าค่าที่จำไว้
            min_val = a[i]      # อัปเดตค่าน้อยที่สุด
        i = i + 1
    return min_val


def find_average(a):
    total = 0
    i = 0
    while i < len(a):
        total = total + a[i]    # บวกสะสมค่าทุกตัวในอะเรย์
        i = i + 1
    return total / len(a)       # ผลรวม หารด้วยจำนวนสมาชิก


# ---------- b. หา index ของค่า max / min ----------

def find_index_max(a):
    idx = 0                     # สมมติว่า index 0 คือตำแหน่งค่ามากที่สุดไว้ก่อน
    i = 1
    while i < len(a):
        if a[i] > a[idx]:       # ถ้าเจอค่าที่มากกว่าค่าที่ index ที่จำไว้
            idx = i             # จำ index ใหม่
        i = i + 1
    return idx


def find_index_min(a):
    idx = 0                     # สมมติว่า index 0 คือตำแหน่งค่าน้อยที่สุดไว้ก่อน
    i = 1
    while i < len(a):
        if a[i] < a[idx]:       # ถ้าเจอค่าที่น้อยกว่าค่าที่ index ที่จำไว้
            idx = i
        i = i + 1
    return idx


# ---------- c. ค้นหาค่าในอะเรย์ (คืนค่า index ที่พบ) ----------

def search_value(a, value):
    i = 0
    while i < len(a):
        if a[i] == value:       # ถ้าค่าที่ตำแหน่ง i ตรงกับค่าที่ต้องการค้นหา
            return i            # คืนค่า index ทันที (ไม่ต้องวนต่อ)
        i = i + 1
    return -1                   # ถ้าวนจนจบแล้วไม่เจอ ให้คืนค่า -1


# ---------- d. นับจำนวนสมาชิกที่มีค่ามากกว่าค่าเฉลี่ย ----------

def count_above_average(a):
    avg = find_average(a)       # หาค่าเฉลี่ยของอะเรย์ก่อน
    count = 0
    i = 0
    while i < len(a):
        if a[i] > avg:          # ถ้าค่าตัวนี้มากกว่าค่าเฉลี่ย
            count = count + 1   # นับเพิ่ม 1
        i = i + 1
    return count


# ---------- e. ตรวจสอบว่าอะเรย์เรียงจากน้อยไปมาก (increasing) หรือไม่ ----------

def is_increasing(a):
    i = 0
    while i < len(a) - 1:       # เทียบทีละคู่ (ตัวปัจจุบัน กับ ตัวถัดไป)
        if a[i] > a[i + 1]:     # ถ้าตัวปัจจุบันมากกว่าตัวถัดไป แสดงว่าไม่เรียงจากน้อยไปมาก
            return False
        i = i + 1
    return True                 # ถ้าวนจนจบไม่เจอกรณีข้างบนเลย แสดงว่าเรียงถูกต้อง


# ---------- หาค่าความแปรปรวน (Variance) ----------
# สูตร: variance = ผลรวมของ (ค่าแต่ละตัว - ค่าเฉลี่ย)^2 ทั้งหมด หารด้วยจำนวนสมาชิก

def find_variance(a):
    n = len(a)
    avg = find_average(a)       # หาค่าเฉลี่ยก่อน
    total = 0
    i = 0
    while i < n:
        diff = a[i] - avg       # ส่วนต่างระหว่างค่าตัวนั้นกับค่าเฉลี่ย
        total = total + diff * diff   # บวกสะสมส่วนต่างยกกำลังสอง
        i = i + 1
    return total / n            # หารด้วยจำนวนสมาชิกทั้งหมด


# ==================== โจทย์เพิ่มเติม (Extra Exercises) ====================

# 1. หาผลรวมของเลขคู่ และผลรวมของเลขคี่ในอะเรย์ แยกกัน
def sum_even_odd(a):
    sum_even = 0
    sum_odd = 0
    i = 0
    while i < len(a):
        if a[i] % 2 == 0:            # ถ้าหารด้วย 2 ลงตัว แสดงว่าเป็นเลขคู่
            sum_even = sum_even + a[i]
        else:                         # ถ้าไม่ลงตัว แสดงว่าเป็นเลขคี่
            sum_odd = sum_odd + a[i]
        i = i + 1
    return sum_even, sum_odd          # คืนค่าทั้งสองผลรวมพร้อมกัน (tuple)

# ---------- ฟังก์ชันหลัก (main) สำหรับทดสอบการทำงาน ----------

def main():
    a = [5, 9, 2, 7, 4, 9, 1]   # ตัวอย่างอะเรย์สำหรับทดสอบ (แก้เป็นชุดของตัวเองได้)
    print("อะเรย์ทั้งหมด:", a)

    print("ค่ามากที่สุด (max) =", find_max(a))
    print("ค่าน้อยที่สุด (min) =", find_min(a))
    print("ค่าเฉลี่ย (average) =", find_average(a))

    print("Index ของค่ามากที่สุด =", find_index_max(a))
    print("Index ของค่าน้อยที่สุด =", find_index_min(a))

    value = int(input("กรอกค่าที่ต้องการค้นหาในอะเรย์: "))
    idx = search_value(a, value)
    if idx == -1:
        print("ไม่พบค่า", value, "ในอะเรย์")
    else:
        print("พบค่า", value, "ที่ index", idx)

    print("จำนวนสมาชิกที่มีค่ามากกว่าค่าเฉลี่ย =", count_above_average(a))
    print("อะเรย์เรียงจากน้อยไปมากหรือไม่ (increasing)?", is_increasing(a))
    print("ค่าความแปรปรวน (variance) =", find_variance(a))


main()