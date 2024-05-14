# mycircle().py
import math
PI = math.pi
xpos, ypos = 0,0

def get_area(radius) : # 원의 면적 계산
    return (PI * radius**2)
def get_peri(radius) : # 원의 둘레 계싼
    return (2 * PI * radius)
def set_pos(x,y) : # 위치 지정
    global xpos,ypos
    xpos,ypos = x,y