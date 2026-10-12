def Promotion():
    print("ใส่ราคาสินค้า 4 ชิ้น")
    i = 0
    k = 0
    sum = 0
    item = []
    while i < 4:
        Get = int(input("ใส่ราคาสินค้า: "))
        if Get >= 1000 and Get <= 2000:
            cal = Get - (Get*(15/100))
        elif Get >= 500 and Get <= 999:
            cal = Get - (Get*(10/100))
        elif Get >= 300 and Get <= 499:
            cal = Get - (Get*(5/100))
        else:
             cal = Get * 1
        item.append(cal)
        print("หลังคำนวณเเล้ว")
        print(item)
        i = i + 1
        while k < len(item):
                sum = sum + item[k] 
                k = k + 1
        print(f"จะต้องจ่ายเงิน: {sum}")
        

def calculate_change(price, cash):
  change = cash - price
  if change < 0:
    print('เงินที่จ่ายมาไม่พอชำระราคาสินค้า')
    return

  print(f'เงินทอนทั้งหมด: {change} บาท\n')

  # กำหนดมูลค่าธนบัตรและเหรียญ
  banknotes = [1000, 500, 100, 50, 20]
  coins = [10, 5, 2, 1]

  print('--- ธนบัตร ---')
  remaining = change
  for note in banknotes:
    count = remaining // note
    remaining %= note
    if count > 0:
      print(f'ธนบัตร {note} บาท: {count} ฉบับ')

  print('\n--- เหรียญ ---')
  for coin in coins:
    count = remaining // coin
    remaining %= coin
    if count > 0:
      print(f'เหรียญ {coin} บาท: {count} เหรียญ')


# ตัวอย่างการใช้งาน: สินค้า 350 บาท จ่ายด้วยเงิน 1000 บาท
calculate_change(350, 1000)
