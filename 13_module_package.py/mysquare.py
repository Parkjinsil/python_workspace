# mysquare.py 정사각형
"""
    mysquare.py: 정사각형의 면적, 둘레, 위치 계산
"""

xpos, ypos = 0,0

def get_area(length): # 정사각형의 면적 계산
    """_summary_
        정사각형의 면적을 구하는 함수
    Args:
        length (float): 정사각형의 한 변의 길이
    Returns:
        float: 정사각형의 면적
    """
    return length**2

def get_peri(length): # 정사각형의 둘레 계산
    """_summary_
        정사각형의 둘레를 구하는 함수
    Args:
        length (float): 정사각형의 한 변의 길이
    Returns:
        float: 정사각형의 둘레
    """
    return 4 * length

def set_pos(x,y):
    global xpos, ypos
    xpos,ypos = x,y