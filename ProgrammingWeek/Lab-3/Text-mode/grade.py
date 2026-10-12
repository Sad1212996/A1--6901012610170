# Lab 3 - Text Ex 2 : Grade
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# คิดเกรดจากคะแนน
#   A = 80-100, B = 70-79, C = 60-69, D = 50-59, F = 0-49

def get_grade(score):
    # เช็คก่อนว่าคะแนนอยู่ในช่วง 0-100 ไหม ถ้าไม่ใช่ส่ง None กลับไป
    if score < 0 or score > 100:
        return None

    # เรียงจากมากไปน้อย เพราะ elif จะหยุดที่เงื่อนไขแรกที่เป็นจริง
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def main():
    score = float(input("Enter your score (0-100): "))
    grade = get_grade(score)

    if grade == None:
        print("Error: score must be between 0 and 100")
    else:
        print("Your grade is", grade)

main()