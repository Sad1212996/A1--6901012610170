# ต่อยอดจากไฟล์ body_temperature.py เดิม
# โจทย์เพิ่ม: หาสถิติรายวัน (รวมทุกสัปดาห์), หาวันที่มีไข้, และเทียบว่าสัปดาห์ไหนอุณหภูมิเสถียรที่สุด

from body_temperature import temperature, week_max, week_min

FEVER_TEMP = 37.5  # อุณหภูมิตั้งแต่นี้ขึ้นไปถือว่ามีไข้


def day_average(d):
    # หาค่าเฉลี่ยอุณหภูมิของวันที่ d รวมทุกสัปดาห์ (d = 0 คือวันแรกของสัปดาห์)
    total = 0
    for week in temperature:
        total += week[d]
    return total / len(temperature)


def day_max(d):
    # หาค่าอุณหภูมิสูงสุดของวันที่ d รวมทุกสัปดาห์
    max_value = temperature[0][d]
    for week in temperature:
        if week[d] > max_value:
            max_value = week[d]
    return max_value


def day_min(d):
    # หาค่าอุณหภูมิต่ำสุดของวันที่ d รวมทุกสัปดาห์
    min_value = temperature[0][d]
    for week in temperature:
        if week[d] < min_value:
            min_value = week[d]
    return min_value


def overall_average():
    # หาค่าเฉลี่ยของอุณหภูมิทั้งหมด ทุกสัปดาห์ทุกวันรวมกัน
    total = 0
    count = 0
    for week in temperature:
        for temp in week:
            total += temp
            count += 1
    return total / count


def find_fever_days():
    # หาว่ามีวันไหนบ้างที่อุณหภูมิถึงเกณฑ์มีไข้ (>= FEVER_TEMP)
    # คืนค่าเป็นลิสต์ของ (สัปดาห์, วัน, อุณหภูมิ)
    fever_days = []
    for w in range(len(temperature)):
        for d in range(len(temperature[w])):
            if temperature[w][d] >= FEVER_TEMP:
                fever_days.append((w, d, temperature[w][d]))
    return fever_days


def most_stable_week():
    # หาสัปดาห์ที่อุณหภูมิเปลี่ยนแปลงน้อยที่สุด (สูงสุด-ต่ำสุดของสัปดาห์นั้นต่างกันน้อยที่สุด)
    best_week = 0
    best_range = week_max(0) - week_min(0)
    for w in range(1, len(temperature)):
        this_range = week_max(w) - week_min(w)
        if this_range < best_range:
            best_range = this_range
            best_week = w
    return best_week


# ทดสอบการทำงาน
for d in range(7):
    print(f"วันที่ {d + 1} ของทุกสัปดาห์ เฉลี่ย = {day_average(d):.2f} สูงสุด = {day_max(d)} ต่ำสุด = {day_min(d)}")

print(f"ค่าเฉลี่ยอุณหภูมิรวมทั้งหมด = {overall_average():.2f}")

fever_list = find_fever_days()
if len(fever_list) == 0:
    print("ไม่พบวันที่มีไข้เลย")
else:
    print(f"พบวันที่มีไข้ทั้งหมด {len(fever_list)} วัน")
    for w, d, temp in fever_list:
        print(f"  สัปดาห์ที่ {w + 1} วันที่ {d + 1} อุณหภูมิ {temp}")

stable_week = most_stable_week()
print(f"สัปดาห์ที่อุณหภูมิเสถียรที่สุดคือสัปดาห์ที่ {stable_week + 1}")
