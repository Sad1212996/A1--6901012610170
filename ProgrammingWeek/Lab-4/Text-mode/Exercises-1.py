# Text Ex 1
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

def multiplication_table():
    # รับค่าแม่สูตรคูณจากผู้ใช้ แปลงเป็นจำนวนเต็ม
    num = int(input("Enter number: "))
    
    # กำหนดค่าเริ่มต้นตัวคูณก่อนเข้า loop[cite: 2]
    i = 1
    
    # ใช้ while loop วนรอบตั้งแต่ 1 ถึง 12
    while i <= 12:
        result = num * i
        # แสดงผลตามรูปแบบที่กำหนด เช่น 3 x 1 = 3
        print(f"{num} x {i} = {result}")
        # ปรับค่าตัวคูณเพิ่มขึ้นทีละ 1[cite: 2]
        i = i + 1

# เรียกใช้ฟังก์ชัน
multiplication_table()