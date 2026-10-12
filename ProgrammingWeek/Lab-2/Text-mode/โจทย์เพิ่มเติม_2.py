# ระบบแคชเชียร์แบบครบวงจร (คิดภาษี + ทอนเงิน)
# สร้างฟังก์ชัน calculate_total(price) เพื่อคำนวณยอดรวมที่บวก VAT 7% แล้ว return ยอดสุทธิกลับออกมา
# สร้างฟังก์ชัน get_change(pay_cash, bill_total) เพื่อคำนวณเงินทอน แล้ว return ค่าเงินทอนกลับออกมา
# สมมติว่าลูกค้าสั่งเมนู berger , pizza , spagetti , coke , water ให้รวมราคาอาหารทุกอย่าง
# นำราคาทีคิดได้ ไปเข้าฟังก์ชันคิด VAT เพื่อหายอดบิลสุทธิ
# รับค่าเงินสดจากลูกค้าผ่าน input()
# นำยอดบิลสุทธิและเงินสดที่รับมา ไปเข้าฟังก์ชันคิดเงินทอน
# ปริ้นต์สรุปใบเสร็จ

# โจทย์จาก Computer bootcamp KMUTNB

# กำหนดราคาอาหาร (คุณครูหรือนักเรียนสามารถเปลี่ยนตัวเลขได้ตามต้องการ)
burger = 89
pizza = 250
spaghetti = 150
coke = 30
water = 15
VAT = 0.07

# 1. สร้างฟังก์ชันคิดราคารวม VAT
def calculate_total(price):
    # คำนวณ vat และ ยอดรวม
    vat = price * VAT
    total = vat + price
    # return ยอดรวมสุทธิกลับออกมา
    return total


# 2. สร้างฟังก์ชันคิดเงินทอน
def get_change(bill_total, pay_cash):
    # return เงินทอนกลับออกมา (เงินลูกค้า - ยอดบิลสุทธิ)
    Change = pay_cash - bill_total
    return Change


# ==========================================
# เริ่มการทำงานของระบบแคชเชียร์
# ==========================================

# 3. รวมราคาอาหารทั้งหมดเข้าด้วยกัน
item1 = calculate_total(pizza)
item2 = calculate_total(burger)
item3 = calculate_total(spaghetti)
item4 = calculate_total(coke)
item5 = calculate_total(water)

total_without_vat = item1 + item2 + item3 + item4 + item5

#print("ราคาอาหารทั้งหมด:",total_without_vat, "บาท")



# 4. เรียกใช้ฟังก์ชัน calculate_total เพื่อหายอดรวม VAT (ส่ง base_price เข้าไป)
total_with_vat = calculate_total(total_without_vat)
#print("ราคาอาหารทั้งหมด(รวมภาษี):",total_with_vat, "บาท")



# 5. รับเงินจากลูกค้า (ใช้ input)
pay = int(input("Your cash: "))

# 6. เรียกใช้ฟังก์ชัน get_change เพื่อหาเงินทอน

Get_change = get_change(total_with_vat, pay)

# 7. ปริ้นต์ใบเสร็จ
print("--- Receipt ---")
print(f"ราคาอาหารสุทธิ:", total_without_vat, "บาท")
print("ยอดรวม (รวม VAT 7%):", total_with_vat, "บาท")
print("รับเงินสด:", pay, "บาท")
print(f"เงินทอน: {Get_change:.2f} บาท")

# Lab 2: Function :L2
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170