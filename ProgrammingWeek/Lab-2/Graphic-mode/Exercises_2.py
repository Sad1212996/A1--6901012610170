from math import sin
from processing import *

def setup():
    size(350,350)

# 2. สร้างฟังก์ชันสําหรับวาดรูปตัวอักษร L , I , N , E โดยให้มีการส่งค่า (parameter/argument)
# สําหรับกําหนดค่าตําแหน่งและขนาดต่างๆเพื่อนําไปใช้ในการคํานวณและสามารถวาดรูปเป็นคําอย่างง่ายได้
# เช่น LINE , INN, NILE, EIN, LININ, NEIL กําหนดให้ใช้ built-in function สําหรับวาด คือ line() เท่านั้น

x = 100
y = 100

def draw():
    global x
    global y
    draw_L()
    draw_I()
    draw_N()
    draw_E()
    
    
def draw_L():
    line(x-40, y, x-40, y+100)
    middle = y + 100
    line(x-40,middle,x+10,middle)
    
def draw_I():
    line(x+25, y, x+25, y+100)
    
def draw_N():
    line(x+40, y, x+40, y+100)
    line(x+40, y, x+80, y+100)
    line(x+80, y, x+80, y+100)
    
def draw_E():
    line(x+95, y, x+95, y+100)
    middle_bottom = y + 100
    line(x+145,middle_bottom,x+95,middle_bottom)
    middle = y + 50
    line(x+145,middle,x+95,middle)
    middle_top = y 
    line(x+145,middle_top,x+95,middle_top)
  
# นายพชรพล ชนะศรี 6901012610170 S.2
run()

# Example taken from Brad Miller's interactivepython.org
# See more here: http://www.skulpt.org/static/proctest.html