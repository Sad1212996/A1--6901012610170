# เกม OX (Tic-Tac-Toe) แบบกราฟิก เขียนด้วย syntax ของ pyp5js
# วิธีรัน: copy โค้ดทั้งหมดไปวางในเว็บ pyp5js demo editor แล้วกด Run
# (ไม่ต้องติดตั้งอะไรเพิ่ม เพราะรันผ่าน pyodide ในเบราว์เซอร์เลย)

CELL = 150  # ขนาดแต่ละช่องบนกระดาน (พิกเซล)

# กระดาน 3x3 เก็บเป็นอาเรย์ 2 มิติ ช่องว่างคือ ""
board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]

current_player = "X"  # ผู้เล่นที่กำลังจะลงตานี้
winner = ""  # ถ้ายังไม่มีคนชนะจะเป็นค่าว่าง


def setup():
    createCanvas(450, 500)


def draw():
    background(255)
    draw_grid()
    draw_marks()
    draw_status()


def draw_grid():
    # วาดเส้นตารางแบ่งช่อง 3x3
    stroke(0)
    strokeWeight(4)
    line(150, 0, 150, 450)
    line(300, 0, 300, 450)
    line(0, 150, 450, 150)
    line(0, 300, 450, 300)


def draw_marks():
    # วาดเครื่องหมาย X หรือ O ตามข้อมูลในกระดาน
    for row in range(3):
        for col in range(3):
            mark = board[row][col]
            x = col * CELL + CELL / 2
            y = row * CELL + CELL / 2
            if mark == "X":
                draw_x(x, y)
            elif mark == "O":
                draw_o(x, y)


def draw_x(x, y):
    stroke(200, 0, 0)
    strokeWeight(6)
    line(x - 40, y - 40, x + 40, y + 40)
    line(x - 40, y + 40, x + 40, y - 40)


def draw_o(x, y):
    stroke(0, 0, 200)
    strokeWeight(6)
    noFill()
    ellipse(x, y, 80, 80)


def draw_status():
    noStroke()
    fill(0)
    textSize(24)
    if winner != "":
        text(f"ผู้ชนะคือ {winner}", 20, 470)
    elif is_board_full():
        text("เสมอกัน", 20, 470)
    else:
        text(f"ตาของผู้เล่น {current_player}", 20, 470)


def mousePressed(event):
    # pyp5js จะส่ง event object ของการคลิกมาให้เสมอ ต้องรับพารามิเตอร์นี้ไว้แม้จะไม่ได้ใช้
    global current_player, winner

    # ถ้าเกมจบไปแล้วก็ไม่ต้องรับคลิกอีก
    if winner != "" or is_board_full():
        return

    col = int(mouseX // CELL)
    row = int(mouseY // CELL)

    if row > 2 or col > 2:
        return

    if board[row][col] == "":
        board[row][col] = current_player
        winner = check_winner()
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def check_winner():
    # เช็คแนวนอนทั้ง 3 แถว
    for row in range(3):
        if board[row][0] != "" and board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]

    # เช็คแนวตั้งทั้ง 3 คอลัมน์
    for col in range(3):
        if board[0][col] != "" and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # เช็คแนวทแยงสองเส้น
    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return ""


def is_board_full():
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True
