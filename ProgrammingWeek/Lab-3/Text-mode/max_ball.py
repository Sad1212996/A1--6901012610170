# Lab 3 - Text Ex 4 : ลูกบอลอะไรมีมากที่สุด
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# รับจำนวนลูก Football, Basketball, Volleyball เก็บในตัวแปร integer 3 ตัว
# แล้วบอกว่าลูกอะไรมีมากที่สุด
# ใช้แค่การเปรียบเทียบพื้นฐาน (ไม่ใช้ max()) เพื่อฝึกคำสั่งเงื่อนไข

def find_most(football, basketball, volleyball):
    # กรณีเท่ากันหมดทั้ง 3 อย่าง
    if football == basketball and basketball == volleyball:
        return "All balls are equal"

    # Football มากที่สุด (หรือเท่ากับอันอื่นที่มากที่สุด)
    if football >= basketball and football >= volleyball:
        # เช็คซ้อนอีกชั้นว่าเสมอกับอันไหนหรือเปล่า
        if football == basketball:
            return "Football and Basketball"
        elif football == volleyball:
            return "Football and Volleyball"
        else:
            return "Football"
    # มาถึงตรงนี้แปลว่า Football ไม่ใช่ที่สุดแล้ว เหลือเทียบ 2 อัน
    elif basketball >= volleyball:
        if basketball == volleyball:
            return "Basketball and Volleyball"
        else:
            return "Basketball"
    else:
        return "Volleyball"

def main():
    football = int(input("Number of Football: "))
    basketball = int(input("Number of Basketball: "))
    volleyball = int(input("Number of Volleyball: "))

    if football < 0 or basketball < 0 or volleyball < 0:
        print("Error: number of balls cannot be negative")
    else:
        print("Most balls:", find_most(football, basketball, volleyball))

main()
