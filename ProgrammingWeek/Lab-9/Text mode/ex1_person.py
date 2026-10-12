# Lab 9 - ข้อ 1 : Person / Student / Employee
# เรื่องการสืบทอดคลาส (Inheritance) และการเขียนทับเมธอด (Method Overriding)
#
# ไอเดียคือ: ข้อมูลที่ "ทุกคน" มีเหมือนกัน (ชื่อ ที่อยู่ น้ำหนัก ส่วนสูง) เก็บไว้ในคลาสแม่ Person
# ส่วนนักเรียนกับพนักงานมีข้อมูลเฉพาะของตัวเองเพิ่มเข้ามา เลยแยกเป็นคลาสลูก
# ทำแบบนี้แล้วไม่ต้องเขียนโค้ดซ้ำ (Code Reuse)


class Person:
    """คลาสแม่ (Superclass) เก็บข้อมูลของคนทั่วไป"""

    def __init__(self, name, address, weight, height):
        # weight หน่วยเป็นกิโลกรัม, height หน่วยเป็นเซนติเมตร
        self.name = name
        self.address = address
        self.weight = weight
        self.height = height

    def getBMI(self):
        # สูตร BMI = น้ำหนัก(kg) / ส่วนสูง(m) ยกกำลังสอง
        # ส่วนสูงเก็บเป็น cm เลยต้องหาร 100 ก่อนให้เป็นเมตร
        height_m = self.height / 100
        return self.weight / (height_m ** 2)

    def show(self):
        # แสดงข้อมูลพื้นฐานของคนคนนี้
        print(f"ชื่อ      : {self.name}")
        print(f"ที่อยู่    : {self.address}")
        print(f"น้ำหนัก   : {self.weight} kg")
        print(f"ส่วนสูง   : {self.height} cm")


class Student(Person):
    """คลาสลูก (Subclass) ของ Person สำหรับเก็บข้อมูลนักเรียน"""

    def __init__(self, name, address, weight, height, student_id, course, gpa):
        # ให้คลาสแม่จัดการข้อมูลส่วนที่เป็นของ Person ไป เราไม่ต้องเขียนเองซ้ำ
        super().__init__(name, address, weight, height)
        # ส่วนนี้คือ attribute ที่เพิ่มมาเฉพาะนักเรียน
        self.student_id = student_id
        self.course = course
        self.gpa = gpa

    def show(self):
        # เขียนทับ (override) show() ของคลาสแม่
        # แต่ยังเรียก show() ของแม่ก่อน เพื่อพิมพ์ข้อมูลพื้นฐานออกมา แล้วค่อยต่อด้วยของนักเรียน
        print("===== ข้อมูลนักเรียน =====")
        super().show()
        print(f"รหัสนักศึกษา : {self.student_id}")
        print(f"หลักสูตร    : {self.course}")
        print(f"GPA        : {self.gpa:.2f}")
        # getBMI() ไม่ได้เขียนไว้ใน Student เลย แต่เรียกได้เพราะสืบทอดมาจาก Person
        print(f"BMI        : {self.getBMI():.2f}")
        print()


class Employee(Person):
    """คลาสลูก (Subclass) ของ Person สำหรับเก็บข้อมูลพนักงาน (หน้าตาคล้าย Student)"""

    def __init__(self, name, address, weight, height, employee_id, department, salary):
        super().__init__(name, address, weight, height)
        # attribute เฉพาะของพนักงาน
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def show(self):
        # override show() เหมือนกับ Student แต่แสดงข้อมูลของพนักงานแทน
        print("===== ข้อมูลพนักงาน =====")
        super().show()
        print(f"รหัสพนักงาน : {self.employee_id}")
        print(f"แผนก       : {self.department}")
        print(f"เงินเดือน   : {self.salary:,.2f} บาท")
        print(f"BMI        : {self.getBMI():.2f}")
        print()


# ---------------- ลองสร้าง object มาทดสอบ ----------------
def main():
    # ฟังก์ชันหลัก รวมโค้ดทดสอบทั้งหมดไว้ที่นี่
    # คนทั่วไป ใช้คลาสแม่ตรง ๆ ได้เลย
    p = Person("สมชาย ใจดี", "กรุงเทพฯ", 70, 175)
    print("===== ข้อมูลบุคคลทั่วไป =====")
    p.show()
    print(f"BMI        : {p.getBMI():.2f}")
    print()

    s = Student("สมหญิง รักเรียน", "นนทบุรี", 50, 160, "6601012345", "Computer Engineering", 3.75)
    s.show()

    e = Employee("สมศักดิ์ ขยันทำงาน", "ปทุมธานี", 85, 170, "EMP001", "IT", 35000)
    e.show()

    # ลองวนลูปเรียก show() ทีละตัว จะเห็นว่าแต่ละคลาสแสดงผลคนละแบบ
    # ทั้งที่เรียกชื่อเมธอดเดียวกัน (นี่คือผลของการ override)
    print("##### วนลูปเรียก show() ของทุกคน #####")
    for person in [s, e]:
        person.show()


# เรียกฟังก์ชัน main() เพื่อเริ่มรันโปรแกรม
main()
