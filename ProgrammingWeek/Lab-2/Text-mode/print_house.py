def print_roof():
    print("  ^  ")
    print(" ^ ^ ")
    print("^   ^")

def print_ceiling():
    print("|||||")

def print_wall():
    print("|   |")
    print("|   |")

def print_floor():
    print("|||||")


def print_house():
    h = int(input("Enter the height of the house: "))
    print_roof()       
    print_ceiling()    
    
    # วนลูปสร้างตัวตึกในแต่ละชั้น (ผนัง + เพดาน)
    for i in range(h):
        print_wall()

        # เช็คเงื่อนไข: ถ้าเป็นชั้นสุดท้ายด้านล่างสุด ให้วาดพื้น (print_floor) 
        # แต่ถ้ายังไม่ถึงชั้นสุดท้าย ให้ใส่เพดานแทรก (print_ceiling)

        if i < h - 1:
            print_ceiling()
        else:
            print_floor()

print_house()

# Lab 2: Function :L2
# นักศึกษา: นายพชรพล ชนะศรี
# รหัสประจำตัว: 6901012610170