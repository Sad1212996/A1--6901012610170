# Lab 3 - โจทย์เพิ่มเติม : ปีอธิกสุรทิน (Leap Year)
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# หาโจทย์มาจากอินเทอร์เน็ต เอามาฝึก nested if + boolean function
# กติกา: ปีที่หาร 4 ลงตัวเป็น leap year
#        แต่ถ้าหาร 100 ลงตัวด้วย ต้องหาร 400 ลงตัวถึงจะเป็น leap year
# เช่น 2024 -> ใช่, 1900 -> ไม่ใช่, 2000 -> ใช่

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main():
    year = int(input("Enter year (A.D.): "))

    if is_leap_year(year):
        print(year, "is a leap year (February has 29 days)")
    else:
        print(year, "is not a leap year (February has 28 days)")

main()
