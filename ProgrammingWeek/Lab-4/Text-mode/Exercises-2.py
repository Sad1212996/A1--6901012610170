# Text Ex 2
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

def find_perfect_numbers(limit):
    # 1. สร้างลิสต์เปล่าสำหรับเก็บตัวเลขที่เป็น "จำนวนสมบูรณ์" (Perfect Number)
    perfect_numbers = []
    
    # 2. วนลูปตรวจสอบทีละตัวเลข ตั้งแต่ 1 ถึง limit (ในที่นี้คือ 50)
    for num in range(1, limit + 1):
        
        # 3. หาตัวหารทั้งหมดของ num (โดยไม่รวมตัวมันเอง)
        # - วนลูป i ตั้งแต่ 1 ถึง num - 1
        # - if num % i == 0 หมายถึง ถ้าหารลงตัว ให้เก็บค่า i ไว้ในลิสต์ divisors
        divisors = [i for i in range(1, num) if num % i == 0]
        
        # 4. เช็คว่า "ผลรวมของตัวหาร" เท่ากับ "ตัวเลขนั้น" หรือไม่
        if sum(divisors) == num:
            # ถ้าผลรวมเท่ากัน แสดงว่าเป็น Perfect Number ให้เพิ่มเข้าลิสต์ผลลัพธ์
            perfect_numbers.append(num)
            
    # 5. ส่งคืนลิสต์จำนวนสมบูรณ์ทั้งหมดที่หาเจอ
    return perfect_numbers

# --- ส่วนการรันโปรแกรม ---

# เรียกใช้ฟังก์ชันเพื่อหาจำนวนสมบูรณ์ในช่วง 1 ถึง 50
result = find_perfect_numbers(50)

# แสดงผลลัพธ์ออกทางหน้าจอ
print(f"Perfect numbers between 1 and 50: {result}")