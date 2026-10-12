# ระบบคำนวณราคาสินค้ารวมภาษี (ระดับเริ่มต้น)
# คำอธิบาย: จงเขียนฟังก์ชันชื่อ calculate_total_price 
# ที่รับพารามิเตอร์ 2 ตัว คือ price (ราคาสินค้า) และ vat_rate (เปอร์เซ็นต์ภาษี เช่น 7) 
# ให้ฟังก์ชันนี้คำนวณและส่งคืน (return) ราคาสินค้าสุทธิที่รวมภาษีแล้ว

def calculate_total_price():
    price = int(input("Enter the price of the product: ")) # รับราคาสินค้า
    vat_rate = int(input("Enter the VAT rate (as a percentage): ")) # รับอัตราภาษี
    vat_amount = price * (vat_rate / 100)
    total_price = price + vat_amount
    return total_price

result = calculate_total_price()  
print("Total price including VAT:", result) 

# Lab 2: Function :L2
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170