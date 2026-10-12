# Lab 3 - Text Ex 1 : BMI
# นักศึกษา: นายพชรพล ชนะศรี L2
# รหัสประจำตัว: 6901012610170

# คำนวณ BMI จากน้ำหนักและส่วนสูง แล้วบอก Weight Status ตามเกณฑ์ของ CDC
#   BMI < 18.5          -> Underweight
#   18.5 <= BMI < 25    -> Healthy Weight
#   25 <= BMI < 30      -> Overweight
#   BMI >= 30           -> Obesity

def calculate_bmi(weight, height_cm):
    # ส่วนสูงรับมาเป็นเซนติเมตร ต้องแปลงเป็นเมตรก่อน
    height_m = height_cm / 100
    return weight / (height_m * height_m)

def weight_status(bmi):
    # ใช้ elif ไล่จากค่าน้อยไปมาก เงื่อนไขไหนจริงก่อนก็ return เลย
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (cm): "))

    # กันค่าที่เป็นไปไม่ได้ เช่น ใส่ 0 จะหารด้วยศูนย์
    if weight <= 0 or height <= 0:
        print("Error: weight and height must be more than 0")
    else:
        bmi = calculate_bmi(weight, height)
        print("Your BMI is", round(bmi, 2))
        print("Weight Status:", weight_status(bmi))

main()
