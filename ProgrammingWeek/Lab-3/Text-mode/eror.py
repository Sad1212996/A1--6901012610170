# Lab 3 - Error ที่เจอระหว่างทำแลป (พร้อมวิธีแก้)
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# 1. SyntaxError: invalid syntax  (เขียน if score = 80:)
# "ใช้ = ซึ่งเป็นการกำหนดค่า แทน == ที่ใช้เปรียบเทียบ"
# วิธีแก้ไข: เปลี่ยนเป็น if score == 80:

# 2. SyntaxError: expected ':'  (เขียน if bmi < 18.5 แล้วลืมใส่ :)
# "ลืมใส่เครื่องหมาย : ท้าย if / elif / else"
# วิธีแก้ไข: ใส่ : ต่อท้ายทุกครั้ง

# 3. IndentationError: expected an indented block
# "คำสั่งที่อยู่ใต้ if ไม่ได้ย่อหน้าเข้าไป"
# วิธีแก้ไข: ย่อหน้าเข้าไป 4 ช่อง ให้เท่ากันทั้งบล็อก

# 4. TypeError: '<' not supported between instances of 'str' and 'int'
# "ลืมแปลง input() เป็นตัวเลข ทำให้เอา string ไปเทียบกับ int"
# วิธีแก้ไข: ใช้ int(input(...)) หรือ float(input(...))

# 5. ValueError: invalid literal for int() with base 10: '65.5'
# "ใส่ทศนิยมแต่ใช้ int() แปลง"
# วิธีแก้ไข: ถ้าค่าอาจมีทศนิยม เช่น น้ำหนัก ส่วนสูง ให้ใช้ float() แทน

# 6. ZeroDivisionError: float division by zero
# "ใส่ส่วนสูงเป็น 0 ตอนคิด BMI"
# วิธีแก้ไข: ใช้ if เช็คก่อนว่าค่ามากกว่า 0 แล้วค่อยคำนวณ

# 7. ผลลัพธ์ผิดแต่ไม่ขึ้น error (Logic Error)
# "เขียน if score >= 50 ไว้ก่อน if score >= 80 ทำให้ได้ D ตลอด"
# วิธีแก้ไข: เรียงเงื่อนไข elif จากมากไปน้อย เพราะ Python หยุดที่เงื่อนไขแรกที่เป็นจริง

# 8. UnboundLocalError ใน draw() ของ processing
# "แก้ค่าตัวแปร x ในฟังก์ชันโดยไม่ได้ประกาศ global"
# วิธีแก้ไข: ใส่ global x ไว้บรรทัดแรกของฟังก์ชัน
