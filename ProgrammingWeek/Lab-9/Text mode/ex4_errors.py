# Lab 9 - สรุป Error ที่เจอบ่อยตอนทำเรื่อง Class / Inheritance พร้อมวิธีแก้
#
# แต่ละข้อจะมี: โค้ดที่ผิด -> error ที่ขึ้น -> สาเหตุ -> วิธีแก้
# ตอนรันไฟล์นี้ จะลองทำให้เกิด error จริงทีละข้อ แล้วจับด้วย try/except
# เพื่อพิมพ์ข้อความ error ออกมาให้ดู (โปรแกรมจะไม่พังกลางทาง)


def demo(title, func):
    # ฟังก์ชันช่วย: เรียกโค้ดที่คาดว่าจะพัง แล้วพิมพ์ชื่อ error ออกมา
    print(f"--- {title} ---")
    try:
        func()
        print("  (ไม่มี error)")
    except Exception as err:
        print(f"  {type(err).__name__}: {err}")
    print()


# ------------------------------------------------------------------
# 1) ลืมใส่ self ในเมธอด
#    TypeError: Person.show() takes 0 positional arguments but 1 was given
#    สาเหตุ: เวลาเรียก p.show() Python ส่งตัว object (self) เข้าไปให้อัตโนมัติ
#            ถ้าเมธอดไม่มีพารามิเตอร์ self มารับ ก็จะเกิน 1 ตัว
#    วิธีแก้: ใส่ self เป็นพารามิเตอร์ตัวแรกของทุกเมธอด -> def show(self):
# ------------------------------------------------------------------
def error_1():
    class Person:
        def show():
            print("hello")

    Person().show()


# ------------------------------------------------------------------
# 2) คลาสลูกเขียน __init__ เอง แต่ลืมเรียก super().__init__()
#    AttributeError: 'Student' object has no attribute 'name'
#    สาเหตุ: พอคลาสลูกมี __init__ ของตัวเอง __init__ ของแม่จะไม่ถูกเรียกให้อัตโนมัติ
#            attribute ที่แม่ควรสร้าง (เช่น name) เลยไม่เคยถูกสร้าง
#    วิธีแก้: เรียก super().__init__(...) ใน __init__ ของคลาสลูก
# ------------------------------------------------------------------
def error_2():
    class Person:
        def __init__(self, name):
            self.name = name

    class Student(Person):
        def __init__(self, name, gpa):
            self.gpa = gpa  # ลืม super().__init__(name)

    s = Student("Tom", 3.5)
    print(s.name)


# ------------------------------------------------------------------
# 3) ส่ง argument ไม่ครบตอนสร้าง object
#    TypeError: Person.__init__() missing 1 required positional argument: 'height'
#    สาเหตุ: __init__ ต้องการ 4 ค่า แต่ส่งไปแค่ 3
#    วิธีแก้: ส่งให้ครบ หรือกำหนดค่า default เช่น def __init__(self, ..., height=0)
# ------------------------------------------------------------------
def error_3():
    class Person:
        def __init__(self, name, address, weight, height):
            self.name = name

    Person("Tom", "BKK", 60)


# ------------------------------------------------------------------
# 4) เรียก super().__init__() แต่ส่ง self ไปด้วย
#    TypeError: Person.__init__() takes 2 positional arguments but 3 were given
#    สาเหตุ: super().__init__ ใส่ self ให้แล้ว ถ้าเราใส่ self เองอีกจะเกินมา 1 ตัว
#    วิธีแก้: super().__init__(name)  (ไม่ต้องใส่ self)
#            ถ้าจะใส่ self ต้องเขียนแบบ Person.__init__(self, name) แทน
# ------------------------------------------------------------------
def error_4():
    class Person:
        def __init__(self, name):
            self.name = name

    class Student(Person):
        def __init__(self, name):
            super().__init__(self, name)

    Student("Tom")


# ------------------------------------------------------------------
# 5) ลืมใส่ self. ตอนอ้างถึง attribute
#    NameError: name 'weight' is not defined
#    สาเหตุ: weight เป็น attribute ของ object ต้องเข้าถึงผ่าน self.weight
#            ถ้าเขียน weight เฉย ๆ Python จะหาเป็นตัวแปรธรรมดาแล้วไม่เจอ
#    วิธีแก้: เขียนเป็น self.weight / self.height
# ------------------------------------------------------------------
def error_5():
    class Person:
        def __init__(self, weight, height):
            self.weight = weight
            self.height = height

        def getBMI(self):
            return weight / (height / 100) ** 2

    Person(60, 170).getBMI()


# ------------------------------------------------------------------
# 6) ส่วนสูงเป็น 0 ตอนคำนวณ BMI
#    ZeroDivisionError: float division by zero
#    สาเหตุ: ข้อมูลส่วนสูงเป็น 0 เลยหารด้วยศูนย์
#    วิธีแก้: เช็กก่อนคำนวณ เช่น if self.height <= 0: return 0
# ------------------------------------------------------------------
def error_6():
    class Person:
        def __init__(self, weight, height):
            self.weight = weight
            self.height = height

        def getBMI(self):
            return self.weight / (self.height / 100) ** 2

    Person(60, 0).getBMI()


# ------------------------------------------------------------------
# 7) เรียกเมธอดที่มีแค่ในคลาสลูก จาก object ของคลาสแม่
#    AttributeError: 'Vehicle' object has no attribute 'seats'
#    สาเหตุ: การสืบทอดเป็นทางเดียว ลูกได้ของจากแม่ แต่แม่ไม่ได้ของจากลูก
#    วิธีแก้: สร้าง object เป็นคลาสลูก (Car) ถ้าต้องการใช้ข้อมูลของลูก
# ------------------------------------------------------------------
def error_7():
    class Vehicle:
        pass

    class Car(Vehicle):
        def __init__(self):
            self.seats = 5

    v = Vehicle()
    print(v.seats)


# ------------------------------------------------------------------
# 8) เอาของที่ไม่มีอยู่ออกจาก list
#    ValueError: list.remove(x): x not in list
#    สาเหตุ: list.remove() จะ error ถ้าหาตัวที่จะลบไม่เจอ
#    วิธีแก้: เช็กก่อนด้วย if item in self.items: แล้วค่อย remove
# ------------------------------------------------------------------
def error_8():
    items = [1, 2, 3]
    items.remove(99)


# ------------------------------------------------------------------
# 9) pop จากคิวว่าง
#    IndexError: pop from empty list
#    สาเหตุ: เรียก items.pop(0) ตอน list ไม่มีของแล้ว
#    วิธีแก้: เช็ก if len(self.items) == 0: ก่อน pop
# ------------------------------------------------------------------
def error_9():
    items = []
    items.pop(0)


# ------------------------------------------------------------------
# 10) ใส่ list ลงใน set ของ Python (ไม่ใช่ mySet)
#    TypeError: unhashable type: 'list'
#    สาเหตุ: set ของ Python เก็บได้แค่ของที่เปลี่ยนค่าไม่ได้ (hashable) เช่น int, str, tuple
#    วิธีแก้: แปลงเป็น tuple ก่อน หรือใช้ mySet ที่เราเขียนเอง (เก็บใน list เลยไม่ติดปัญหานี้)
# ------------------------------------------------------------------
def error_10():
    s = set()
    s.add([1, 2])


# ------------------------------------------------------------------
# 11) Error ที่ไม่ได้ขึ้นตอนรัน แต่เจอตอนเขียน:
#    - IndentationError: expected an indented block
#        ลืมย่อหน้าโค้ดใต้ class / def  -> ย่อหน้า 4 ช่องให้ตรงกัน
#    - SyntaxError: expected ':'
#        ลืมใส่ : หลัง class Car(Vehicle) หรือ def show(self) -> เติม : ท้ายบรรทัด
#    - ModuleNotFoundError: No module named 'ex1_person'
#        import ไฟล์อื่นแต่รันจากโฟลเดอร์อื่น -> cd เข้าโฟลเดอร์ที่มีไฟล์ก่อนแล้วค่อยรัน
#    ข้อพวกนี้ทำให้ไฟล์ทั้งไฟล์รันไม่ได้เลย จึงไม่ได้ใส่เป็นตัวอย่างให้รันจริง
# ------------------------------------------------------------------


def main():
    # ฟังก์ชันหลัก รวมโค้ดทดสอบทั้งหมดไว้ที่นี่
    demo("1) ลืม self", error_1)
    demo("2) ลืม super().__init__()", error_2)
    demo("3) ส่ง argument ไม่ครบ", error_3)
    demo("4) ใส่ self ใน super().__init__()", error_4)
    demo("5) ลืม self. หน้า attribute", error_5)
    demo("6) หารด้วยศูนย์", error_6)
    demo("7) แม่เรียกของที่มีแค่ในลูก", error_7)
    demo("8) remove ของที่ไม่มี", error_8)
    demo("9) pop จาก list ว่าง", error_9)
    demo("10) ใส่ list ลง set", error_10)


# เรียกฟังก์ชัน main() เพื่อเริ่มรันโปรแกรม
main()
