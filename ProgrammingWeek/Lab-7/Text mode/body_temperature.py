# โปรแกรมเก็บข้อมูลอุณหภูมิร่างกาย 4 สัปดาห์ สัปดาห์ละ 7 วัน
# เก็บข้อมูลเป็นอาเรย์ 2 มิติ -> แต่ละแถวคือ 1 สัปดาห์, แต่ละคอลัมน์คือ 1 วัน

# ข้อมูลตัวอย่าง (หน่วยองศาเซลเซียส) สมมติขึ้นมาเพื่อทดสอบโปรแกรม
temperature = [
    [36.5, 36.7, 37.0, 36.8, 36.6, 36.9, 37.1],  # สัปดาห์ที่ 1 -> w = 0
    [36.4, 36.6, 36.5, 36.9, 37.2, 36.8, 36.7],  # สัปดาห์ที่ 2 -> w = 1
    [36.9, 37.0, 36.8, 36.6, 36.5, 36.7, 36.9],  # สัปดาห์ที่ 3 -> w = 2
    [36.6, 36.5, 36.7, 36.8, 37.3, 36.9, 36.6],  # สัปดาห์ที่ 4 -> w = 3
]


def week_average(w):
    # หาค่าเฉลี่ยอุณหภูมิของสัปดาห์ที่ w (w = 0 คือสัปดาห์แรก)
    week_data = temperature[w]
    return sum(week_data) / len(week_data)


def week_max(w):
    # หาค่าอุณหภูมิสูงสุดของสัปดาห์ที่ w
    return max(temperature[w])


def week_min(w):
    # หาค่าอุณหภูมิต่ำสุดของสัปดาห์ที่ w
    return min(temperature[w])


def overall_max():
    # หาค่าอุณหภูมิสูงสุดจากข้อมูลทั้งหมด
    max_value = week_max(0)
    for w in range(1, len(temperature)):
        if week_max(w) > max_value:
            max_value = week_max(w)
    return max_value


def overall_min():
    # หาค่าอุณหภูมิต่ำสุดจากข้อมูลทั้งหมด
    min_value = week_min(0)
    for w in range(1, len(temperature)):
        if week_min(w) < min_value:
            min_value = week_min(w)
    return min_value


# ทดสอบการทำงานของฟังก์ชันทั้งหมด
print(f"สัปดาห์ที่ 1 เฉลี่ย {week_average(0)} สูงสุด {week_max(0)} ต่ำสุด {week_min(0)}")
print(f"สัปดาห์ที่ 2 เฉลี่ย {week_average(1)} สูงสุด {week_max(1)} ต่ำสุด {week_min(1)}")
print(f"สัปดาห์ที่ 3 เฉลี่ย {week_average(2)} สูงสุด {week_max(2)} ต่ำสุด {week_min(2)}")
print(f"สัปดาห์ที่ 4 เฉลี่ย {week_average(3)} สูงสุด {week_max(3)} ต่ำสุด {week_min(3)}")

print(f"อุณหภูมิสูงสุดตลอด 4 สัปดาห์ = {overall_max()}")
print(f"อุณหภูมิต่ำสุดตลอด 4 สัปดาห์ = {overall_min()}")
