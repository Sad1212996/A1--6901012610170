# Text Ex 4
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

# โปรแกรมคำนวณจำนวนและน้ำหนักเฉลี่ยของทุเรียน

total_count = 0   # ตัวแปรเก็บจำนวนลูกทุเรียนทั้งหมด
total_weight = 0  # ตัวแปรเก็บผลรวมน้ำหนักทุเรียนทั้งหมด

while True:
    # รับค่าน้ำหนักทุเรียนจากผู้ใช้
    weight = float(input("Please input Durian weight: "))
    
    # ถ้าป้อนค่าเป็น 0 แสดงว่าป้อนครบแล้ว ให้หยุดการทำงานของลูป
    if weight == 0:
        break
    
    # เพิ่มจำนวนลูกทุเรียนสะสมทีละ 1
    total_count += 1
    
    # บวกสะสมน้ำหนักทุเรียนเข้าตัวแปร total_weight
    total_weight += weight

print() # เว้นบรรทัดให้สวยงามตรงตามตัวอย่าง

# แสดงผลลัพธ์จำนวนลูกทุเรียนทั้งหมด
print(f"Total of {total_count} Durians")

# คำนวณและแสดงผลน้ำหนักเฉลี่ย (เช็คป้องกันกรณีไม่ได้ใส่ทุเรียนเลยแล้วกด 0)
if total_count > 0:
    avg_weight = total_weight / total_count
    # แสดงผลค่าเฉลี่ย (ตัดทศนิยมถ้าเป็นจำนวนเต็มตามตัวอย่างโจทย์)
    if avg_weight.is_integer():
        print(f"Average weight is {int(avg_weight)}")
    else:
        print(f"Average weight is {avg_weight:.2f}")
else:
    print("Average weight is 0")