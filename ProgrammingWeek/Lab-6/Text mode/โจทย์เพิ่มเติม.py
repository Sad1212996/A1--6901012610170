# Lab 6
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170

# ---------- กลับลำดับตัวอักษรในสตริง (reverse) ----------
def reverse_string(s):
    result = ""
    i = len(s) - 1              # เริ่มจากตัวอักษรสุดท้ายของ s
    while i >= 0:
        result = result + s[i]  # ต่อท้ายผลลัพธ์ด้วยตัวอักษรจากท้ายมาหน้า
        i = i - 1
    return result


def main():
    s = "Thailand"
    print("ข้อความเดิม:", s)
    print("ข้อความที่กลับลำดับ:", reverse_string(s))



main()