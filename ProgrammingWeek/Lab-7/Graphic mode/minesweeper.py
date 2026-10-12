# เกม Minesweeper (กู้ระเบิด) แบบกราฟิก เขียนด้วย syntax ของ pyp5js
# วิธีรัน: copy โค้ดทั้งหมดไปวางในเว็บ pyp5js demo editor แล้วกด Run
# วิธีเล่น: คลิกซ้ายเพื่อเปิดช่อง, คลิกขวาเพื่อปักธงช่องที่คิดว่ามีระเบิด

import random as pyrandom  # pyp5js มี random() ของตัวเองอยู่แล้ว ตั้งชื่อ import แยกกันไม่ให้ชนกัน

ROWS = 8
COLS = 8
MINE_COUNT = 10
CELL = 50

# อาเรย์ 2 มิติเก็บสถานะของแต่ละช่อง
mine_grid = [[False for _ in range(COLS)] for _ in range(ROWS)]      # ช่องนี้มีระเบิดไหม
revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]       # ช่องนี้เปิดแล้วหรือยัง
flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]        # ช่องนี้ถูกปักธงไหม
neighbor_mines = [[0 for _ in range(COLS)] for _ in range(ROWS)]     # จำนวนระเบิดรอบๆ ช่องนี้

game_over = False
game_win = False


def place_mines():
    # สุ่มวางระเบิดลงในกระดาน จำนวน MINE_COUNT ลูก
    placed = 0
    while placed < MINE_COUNT:
        r = pyrandom.randint(0, ROWS - 1)
        c = pyrandom.randint(0, COLS - 1)
        if not mine_grid[r][c]:
            mine_grid[r][c] = True
            placed += 1


def count_neighbor_mines():
    # นับจำนวนระเบิดที่อยู่รอบๆ ทุกช่อง (8 ทิศ)
    for r in range(ROWS):
        for c in range(COLS):
            if mine_grid[r][c]:
                continue
            total = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and mine_grid[nr][nc]:
                        total += 1
            neighbor_mines[r][c] = total


def reveal_cell(r, c):
    # เปิดช่อง (r, c) ถ้ารอบๆ ไม่มีระเบิดเลยให้เปิดช่องข้างเคียงต่อไปเรื่อยๆ
    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return
    if revealed[r][c] or flagged[r][c]:
        return

    revealed[r][c] = True

    if not mine_grid[r][c] and neighbor_mines[r][c] == 0:
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr != 0 or dc != 0:
                    reveal_cell(r + dr, c + dc)


def reveal_all_mines():
    for r in range(ROWS):
        for c in range(COLS):
            if mine_grid[r][c]:
                revealed[r][c] = True


def check_win():
    # ชนะเมื่อช่องที่ไม่มีระเบิดถูกเปิดจนหมด
    for r in range(ROWS):
        for c in range(COLS):
            if not mine_grid[r][c] and not revealed[r][c]:
                return False
    return True


def setup():
    createCanvas(COLS * CELL, ROWS * CELL + 40)
    place_mines()
    count_neighbor_mines()


def draw():
    background(230)
    draw_board()
    draw_status()


def draw_board():
    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL
            y = r * CELL
            stroke(120)
            strokeWeight(1)

            if revealed[r][c]:
                if mine_grid[r][c]:
                    fill(220, 60, 60)
                else:
                    fill(240)
                rect(x, y, CELL, CELL)

                if not mine_grid[r][c] and neighbor_mines[r][c] > 0:
                    noStroke()
                    fill(20, 20, 160)
                    textSize(20)
                    text(str(neighbor_mines[r][c]), x + 18, y + 14)
            else:
                if (r + c) % 2 == 0:
                    fill(110, 190, 110)
                else:
                    fill(95, 170, 95)
                rect(x, y, CELL, CELL)

                if flagged[r][c]:
                    noStroke()
                    fill(230, 170, 0)
                    textSize(20)
                    text("F", x + 18, y + 14)


def draw_status():
    noStroke()
    fill(0)
    textSize(18)
    if game_over:
        text("เหยียบระเบิดเข้าแล้ว เกมจบ!", 10, ROWS * CELL + 10)
    elif game_win:
        text("กู้ระเบิดสำเร็จ ชนะแล้ว!", 10, ROWS * CELL + 10)
    else:
        text("คลิกซ้ายเปิดช่อง / คลิกขวาปักธง", 10, ROWS * CELL + 10)


def mousePressed(event):
    # pyp5js จะส่ง event object ของการคลิกมาให้เสมอ ต้องรับพารามิเตอร์นี้ไว้แม้จะไม่ได้ใช้
    global game_over, game_win

    if game_over or game_win:
        return

    col = int(mouseX // CELL)
    row = int(mouseY // CELL)

    if row >= ROWS or col >= COLS:
        return

    if mouseButton == RIGHT:
        # คลิกขวา = ปักธง/เอาธงออก (เฉพาะช่องที่ยังไม่เปิด)
        if not revealed[row][col]:
            flagged[row][col] = not flagged[row][col]
        return

    # คลิกซ้าย = เปิดช่อง (ถ้าปักธงไว้จะเปิดไม่ได้ ต้องเอาธงออกก่อน)
    if flagged[row][col]:
        return

    reveal_cell(row, col)

    if mine_grid[row][col]:
        game_over = True
        reveal_all_mines()
    elif check_win():
        game_win = True
