# Lab 9 - ข้อ 3 : สร้างคลาส Collection ของตัวเอง (mySet, myBag, myQueue)
# ทุกคลาสมีเมธอด show(), add(), remove()
#
# ทั้งสามแบบเก็บของไว้ใน list เหมือนกัน และ show() ก็เหมือนกัน
# เลยทำคลาสแม่ myCollection ไว้ก่อน แล้วให้แต่ละแบบสืบทอดไป
# จากนั้นค่อย override เฉพาะส่วนที่ทำงานต่างกัน
#
# ใบงานให้เริ่มจากเก็บ "ตัวเลข (int)" ก่อน แล้วค่อยลองเก็บ "object ชนิดอะไรก็ได้"
# เนื่องจาก list ใน Python เก็บของได้ทุกชนิดอยู่แล้ว โค้ดชุดนี้เลยใช้ได้ทั้งสองแบบ


class myCollection:
    """คลาสแม่ของ collection ทุกแบบ"""

    def __init__(self):
        # list ว่างไว้เก็บของ
        self.items = []

    def show(self):
        # แสดงชื่อคลาส + ของที่อยู่ข้างใน
        # type(self).__name__ จะได้ชื่อคลาสลูกที่เรียกใช้จริง เช่น mySet, myBag
        print(f"{type(self).__name__} ({len(self.items)} items): {self.items}")

    def add(self, item):
        # แบบพื้นฐาน: ใส่ต่อท้ายไปเลย
        self.items.append(item)

    def remove(self, item):
        # แบบพื้นฐาน: ลบตัวที่เจอตัวแรกออก ถ้าไม่มีก็แจ้งเตือน (ไม่ให้โปรแกรมพัง)
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"  ! ไม่พบ {item!r} ใน {type(self).__name__}")


class mySet(myCollection):
    """เซต: ห้ามมีของซ้ำ"""

    def add(self, item):
        # override add() - เช็กก่อนว่ามีอยู่แล้วหรือยัง ถ้ามีแล้วไม่ใส่ซ้ำ
        if item in self.items:
            print(f"  ! {item!r} มีอยู่ใน mySet แล้ว ไม่เพิ่มซ้ำ")
        else:
            super().add(item)

    # remove() ใช้ของคลาสแม่ได้เลย เพราะเซตมีของแต่ละตัวแค่ชิ้นเดียวอยู่แล้ว


class myBag(myCollection):
    """ถุง (Bag / Multiset): ใส่ของซ้ำได้ ลำดับไม่สำคัญ"""

    # add() กับ remove() ใช้ของคลาสแม่ได้ตรง ๆ
    # (add ใส่ซ้ำได้, remove ลบออกทีละชิ้น)
    # เพิ่มเมธอดนับจำนวน ว่าของชิ้นนั้นมีอยู่ในถุงกี่ชิ้น

    def count(self, item):
        return self.items.count(item)


class myQueue(myCollection):
    """คิว: เข้าก่อน ออกก่อน (FIFO - First In First Out)"""

    # add() ใช้ของแม่ได้เลย เพราะการเข้าคิวคือการต่อท้าย

    def remove(self):
        # override remove() - คิวไม่ได้เลือกว่าจะเอาตัวไหนออก
        # แต่จะเอาตัวที่อยู่หัวคิว (ตัวแรกสุด) ออกเสมอ แล้วคืนค่าตัวนั้นกลับไป
        if len(self.items) == 0:
            print("  ! คิวว่าง ไม่มีอะไรให้เอาออก")
            return None
        return self.items.pop(0)


class Student:
    """คลาสง่าย ๆ ไว้ทดสอบว่า collection เก็บ object ที่เราสร้างเองได้"""

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        # กำหนดว่าตอน print ออกมาใน list จะให้หน้าตาเป็นยังไง
        # ถ้าไม่เขียนไว้ จะขึ้นเป็น <Student object at 0x...> อ่านไม่รู้เรื่อง
        return f"Student({self.name}, {self.student_id})"


# ---------------- ลองทดสอบ ----------------
def main():
    # ฟังก์ชันหลัก รวมโค้ดทดสอบทั้งหมดไว้ที่นี่
    print("########## ขั้นที่ 1 : เก็บตัวเลข (int) ##########")

    s = mySet()
    for n in [3, 1, 4, 1, 5]:  # เลข 1 ใส่สองครั้ง ครั้งที่สองต้องไม่เข้า
        s.add(n)
    s.show()
    s.remove(4)
    s.remove(99)  # ลบตัวที่ไม่มี
    s.show()
    print()

    b = myBag()
    for n in [3, 1, 4, 1, 5]:  # ถุงใส่ซ้ำได้
        b.add(n)
    b.show()
    print(f"  เลข 1 อยู่ในถุง {b.count(1)} ชิ้น")
    b.remove(1)  # ลบออกไปแค่ชิ้นเดียว
    b.show()
    print()

    q = myQueue()
    for n in [10, 20, 30]:
        q.add(n)
    q.show()
    print(f"  เอาออกจากคิว: {q.remove()}")  # ต้องได้ 10 เพราะเข้ามาก่อน
    q.show()
    print()

    print("########## ขั้นที่ 2 : เก็บ object ชนิดไหนก็ได้ ##########")

    # ลองเอา object ของคลาสที่เราสร้างเอง (Student ด้านบนไฟล์) มาใส่ในคิวด้วย
    stu = Student("สมหญิง", "6601012345")

    s2 = mySet()
    for x in ["apple", 3.14, (1, 2), "apple", True]:
        s2.add(x)
    s2.show()
    print()

    b2 = myBag()
    for x in ["cat", "dog", "cat", [1, 2]]:
        b2.add(x)
    b2.show()
    print()

    q2 = myQueue()
    q2.add("ลูกค้าคนที่ 1")
    q2.add(stu)
    q2.add({"order": 42})
    q2.show()
    first = q2.remove()
    second = q2.remove()
    print(f"  ออกคิวคนแรก : {first}")
    print(f"  ออกคิวคนที่สอง เป็น {type(second).__name__} ชื่อ {second.name}")
    q2.show()
    q2.remove()
    q2.remove()  # คิวว่างแล้ว ลองเอาออกอีกรอบ


# เรียกฟังก์ชัน main() เพื่อเริ่มรันโปรแกรม
main()
