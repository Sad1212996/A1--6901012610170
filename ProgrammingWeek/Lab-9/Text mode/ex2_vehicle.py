# Lab 9 - ข้อ 2 : Vehicle / Car / Truck (ระบบรถให้เช่า)
# หมายเหตุ: ในใบงานสะกดว่า "Vihicle" แต่ในโค้ดใช้ตัวสะกดที่ถูกคือ "Vehicle"
#
# คลาสแม่ Vehicle เก็บข้อมูลที่รถทุกคันต้องมี
# คลาสลูก Car กับ Truck เพิ่มข้อมูลเฉพาะของตัวเอง และคิดค่าเช่าต่างกัน


class Vehicle:
    """คลาสแม่ (Superclass) ของรถให้เช่าทุกประเภท"""

    def __init__(self, license_plate, brand, model, year, daily_rate):
        self.license_plate = license_plate  # ป้ายทะเบียน
        self.brand = brand                  # ยี่ห้อ
        self.model = model                  # รุ่น
        self.year = year                    # ปีที่ผลิต
        self.daily_rate = daily_rate        # ค่าเช่าต่อวัน (บาท)

    def show_info(self):
        # แสดงข้อมูลพื้นฐานของรถคันนี้
        print(f"ทะเบียน      : {self.license_plate}")
        print(f"ยี่ห้อ/รุ่น    : {self.brand} {self.model}")
        print(f"ปี           : {self.year}")
        print(f"ค่าเช่า/วัน   : {self.daily_rate:,.2f} บาท")

    def calculate_rental_cost(self, days):
        # ค่าเช่าแบบปกติ = ค่าเช่าต่อวัน x จำนวนวัน
        return self.daily_rate * days


class Car(Vehicle):
    """รถยนต์นั่ง - มีจำนวนที่นั่ง และได้โปรเช่า 5 แถม 2"""

    def __init__(self, license_plate, brand, model, year, daily_rate, seats):
        # ส่วนข้อมูลพื้นฐานให้คลาสแม่จัดการ
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.seats = seats  # จำนวนที่นั่ง

    def show_info(self):
        # เรียก show_info() ของแม่ก่อน แล้วค่อยเพิ่มข้อมูลของรถยนต์นั่ง
        print("===== รถยนต์นั่ง (Car) =====")
        super().show_info()
        print(f"จำนวนที่นั่ง  : {self.seats} ที่นั่ง")

    def calculate_rental_cost(self, days):
        # โปรโมชั่น: เช่า 5 วัน แถมฟรี 2 วัน (ใช้ได้ 7 วัน แต่จ่ายแค่ 5 วัน)
        # คิดเป็นรอบละ 7 วัน -> ทุก ๆ 7 วันจ่ายแค่ 5 วัน
        #   เช่น 7 วัน  = จ่าย 5 วัน
        #        9 วัน  = 1 รอบ (จ่าย 5) + เศษ 2 วัน (จ่าย 2) = จ่าย 7 วัน
        #        14 วัน = 2 รอบ = จ่าย 10 วัน
        # ถ้าเศษเกิน 5 วัน (เช่นเศษ 6 วัน) ก็ถือว่าอยู่ในช่วงวันฟรีแล้ว จ่ายแค่ 5
        full_weeks = days // 7
        remaining = days % 7
        paid_days = full_weeks * 5 + min(remaining, 5)
        # คิดเงินด้วยสูตรของคลาสแม่ แค่เปลี่ยนจำนวนวันเป็นวันที่ต้องจ่ายจริง
        return super().calculate_rental_cost(paid_days)


class Truck(Vehicle):
    """รถบรรทุก - มีน้ำหนักบรรทุก และไม่มีโปรโมชั่น"""

    def __init__(self, license_plate, brand, model, year, daily_rate, payload):
        super().__init__(license_plate, brand, model, year, daily_rate)
        self.payload = payload  # น้ำหนักบรรทุก (ตัน)

    def show_info(self):
        print("===== รถบรรทุก (Truck) =====")
        super().show_info()
        print(f"น้ำหนักบรรทุก : {self.payload} ตัน")

    # Truck ไม่ต้องเขียน calculate_rental_cost() ใหม่
    # เพราะคิดค่าเช่าแบบปกติ ใช้ของคลาสแม่ที่สืบทอดมาได้เลย


# ---------------- ลองสร้าง object มาทดสอบ ----------------
def main():
    # ฟังก์ชันหลัก รวมโค้ดทดสอบทั้งหมดไว้ที่นี่
    car = Car("กข 1234", "Toyota", "Yaris", 2022, 1200, 5)
    truck = Truck("80-5678", "Isuzu", "D-Max", 2020, 2000, 1.5)

    # ลองเช่าหลาย ๆ จำนวนวัน จะได้เห็นว่าโปรของ Car ทำงานถูกไหม
    test_days = [3, 5, 7, 9, 14]

    for vehicle in [car, truck]:
        vehicle.show_info()
        print("--- ค่าเช่า ---")
        for d in test_days:
            cost = vehicle.calculate_rental_cost(d)
            print(f"เช่า {d:>2} วัน : {cost:>10,.2f} บาท")
        print()


# เรียกฟังก์ชัน main() เพื่อเริ่มรันโปรแกรม
main()
