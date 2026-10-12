# โปรแกรมจัดการอาเรย์ 2 มิติ / เมทริกซ์
# มีฟังก์ชันหาค่ามากสุด-น้อยสุด-เฉลี่ย, ค้นหาค่าในอาเรย์, และคำนวณเมทริกซ์ (บวก ลบ คูณ)

my_array = [
    [12, 45, 7, 89],
    [33, 55, 21, 4],
    [67, 18, 90, 26],
]


def find_max(array):
    # หาค่ามากที่สุดในอาเรย์ 2 มิติ โดยวนเช็คทุกแถวทุกคอลัมน์
    max_value = array[0][0]
    for row in array:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value


def find_min(array):
    # หาค่าน้อยที่สุดในอาเรย์ 2 มิติ โดยวนเช็คทุกแถวทุกคอลัมน์
    min_value = array[0][0]
    for row in array:
        for value in row:
            if value < min_value:
                min_value = value
    return min_value


def find_average(array):
    # หาค่าเฉลี่ยของค่าทั้งหมดในอาเรย์ 2 มิติ
    total = 0
    count = 0
    for row in array:
        for value in row:
            total += value
            count += 1
    return total / count


def is_found(array, target):
    # เช็คว่ามีค่า target อยู่ในอาเรย์ 2 มิติหรือไม่ คืนค่าเป็น True/False
    for row in array:
        for value in row:
            if value == target:
                return True
    return False


def matrix_add(a, b):
    # บวกเมทริกซ์ a กับ b ทีละตำแหน่ง (ต้องมีขนาดเท่ากัน)
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result


def matrix_subtract(a, b):
    # ลบเมทริกซ์ a กับ b ทีละตำแหน่ง (ต้องมีขนาดเท่ากัน)
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])
        result.append(row)
    return result


def matrix_multiply(a, b):
    # คูณเมทริกซ์ a กับ b แบบเมทริกซ์จริง (จำนวนคอลัมน์ของ a ต้องเท่ากับจำนวนแถวของ b)
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = 0
            for k in range(len(b)):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result


# ทดสอบฟังก์ชันเกี่ยวกับอาเรย์ 2 มิติ
print(f"อาเรย์ตัวอย่าง = {my_array}")
print(f"ค่ามากที่สุด = {find_max(my_array)}")
print(f"ค่าน้อยที่สุด = {find_min(my_array)}")
print(f"ค่าเฉลี่ย = {find_average(my_array)}")
print(f"มีค่า 55 อยู่ในอาเรย์หรือไม่ = {is_found(my_array, 55)}")
print(f"มีค่า 100 อยู่ในอาเรย์หรือไม่ = {is_found(my_array, 100)}")

# ทดสอบการคำนวณเมทริกซ์
matrix_a = [
    [1, 2],
    [3, 4],
]

matrix_b = [
    [5, 6],
    [7, 8],
]

print(f"เมทริกซ์ A = {matrix_a}")
print(f"เมทริกซ์ B = {matrix_b}")
print(f"A + B = {matrix_add(matrix_a, matrix_b)}")
print(f"A - B = {matrix_subtract(matrix_a, matrix_b)}")
print(f"A x B = {matrix_multiply(matrix_a, matrix_b)}")
