# Lab 3 - Text Ex 3 : พื้นที่ที่ดินสี่เหลี่ยม
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# รับความกว้างและความยาวของที่ดิน (เมตร) แสดงพื้นที่เป็นตารางเมตร
# แล้วบอกว่าพอสำหรับสนามกีฬาอะไรได้บ้าง
# ใช้ boolean function (can_fit) ตามที่บทที่ 6 บอกให้ลองทำ

# ขนาดสนามมาตรฐาน (กว้าง x ยาว) หน่วยเมตร
#   Football   68 x 105
#   Basketball 15 x 28
#   Tennis     10.97 x 23.77
#   Volleyball 9 x 18
#   Badminton  6.1 x 13.4

def calculate_area(width, length):
    return width * length

def can_fit(width, length, field_w, field_l):
    # ส่ง True กลับไปถ้าวางสนามลงในที่ดินได้
    # ลองวางทั้งแนวปกติ และหมุน 90 องศา เพราะบางทีคนใส่กว้าง/ยาวสลับกัน
    if width >= field_w and length >= field_l:
        return True
    elif width >= field_l and length >= field_w:
        return True
    else:
        return False

def main():
    width = float(input("Enter land width (m): "))
    length = float(input("Enter land length (m): "))

    if width <= 0 or length <= 0:
        print("Error: width and length must be more than 0")
        return

    area = calculate_area(width, length)
    print("Land area =", round(area, 2), "square meters")
    print("This land is enough for:")

    # เอาไว้เช็คว่ามีกีฬาที่เล่นได้อย่างน้อย 1 อย่างไหม
    found = False

    if can_fit(width, length, 68, 105):
        print("- Football")
        found = True
    if can_fit(width, length, 15, 28):
        print("- Basketball")
        found = True
    if can_fit(width, length, 10.97, 23.77):
        print("- Tennis")
        found = True
    if can_fit(width, length, 9, 18):
        print("- Volleyball")
        found = True
    if can_fit(width, length, 6.1, 13.4):
        print("- Badminton")
        found = True

    if not found:
        print("- Nothing, the land is too small")

main()
