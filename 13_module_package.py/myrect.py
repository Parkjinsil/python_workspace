# myrect().py
xpos, ypos = 0,0

def get_area(width,height): # 사각형 면적 계산
    area = width * height
    return area

def get_peri(width, height): # 사각형 둘레 계산
    peri = 2 * (width + height)
    return peri

def set_pos(x,y): # 위치 지정
    global xpos,ypos
    xpos,ypos = x,y