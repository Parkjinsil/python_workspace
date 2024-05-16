'''
모듈(Module)
: 재사용을 목적으로 작성된 특정한 기능을 수행하는 코드들의 집합

패키지(Package)
: 관련있는 모듈들의 모음
  ex) NumPy, SciPy, Matplotlib, Pandas...
  
Pillow (Python Imaging Library ,PIL)
: 많은 영상 포맷 지원

이미지 포맷
JPG/Jpeg 이미지 압축 효율 좋음
BMP : Bitmap 압축 안함 매우 큼
PNG : 투명도 필요한 파일
'''

# PIL 모듈에서 몇 개의 클래스를 포함시킨다./ tkinter 모듈을 포함시킨다.
from PIL import Image, ImageTk
import tkinter as tk

# 영상 표시
# 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다.
# window = tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# # 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다.
# img = Image.open("C:/doit/dog.png")

# # tk 형식으로 영상을 변환한다.
# tk_img = ImageTk.PhotoImage(img)

# # tkinter의 캔버스에 영상을 표시한다.
# canvas.create_image(250,250,image=tk_img)

# window.mainloop()

# print('--------------------------------------------------')

# # 영상 45도 회전 후 표시
# window = tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# # 영상 파일을 연다
# im = Image.open("C:/doit/dog.png")

# # 영상을 45도 회전한다.
# out = im.rotate(45)

# # 영상을 tkinter 형식으로 변환한다.
# tk_img = ImageTk.PhotoImage(out)

# # 영상을 tkinter에서 화면에 표시한다.
# canvas.create_image(250,250,image=tk_img)
# window.mainloop()

# print('--------------------------------------------------')

from PIL import ImageFilter
# # 영상 흐리게 한 후 표시
# window = tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# # 영상 파일을 연다.
# im = Image.open('C:/doit/dog.png')

# # 영상을 흐리게 한다
# out = im.filter(ImageFilter.BLUR)

# # 영상을 tkinter 형식으로 변환한다.
# tk_img = ImageTk.PhotoImage(out)

# # 영상을 tkinter에서 화면에 표시한다.
# canvas.create_image(250,250,image=tk_img)
# window.mainloop()

# print('--------------------------------------------------')

# def open():
#     pass

# def quit():
#     window.quit()
    
# window = tk.Tk()
# menubar = tk.Menu(window)

# filemenu = tk.Menu(menubar)
# filemenu.add_command(label='열기', command=open)
# filemenu.add_command(label='종료', command=quit)

# menubar.add_cascade(label='파일', menu=filemenu)

# window.config(menu=menubar)
# window.mainloop()
    
print('====================================================')
# 영상 처리 기능을 메뉴로 연결
from tkinter import filedialog as fd

# im = None
# tk_img = None

# # 파일 메뉴에서 '열기'를 선택하였을 때 호출되는 함수 def
# def open():
#     global im,tk_img
#     fname = fd.askopenfilename() # 내가 고른 파일 경로를 변수에 저장
#     im = Image.open(fname)       # 파일 경로로 이미지 파일을 열고 이를 변수에 저장
#     tk_img = ImageTk.PhotoImage(im)  # 이미지를 tkinter 형식으로 변환하고 변수에 저장
#     canvas.create_image(250,250,image=tk_img) # 캔버스의 (250,250)위치에 이미지 표시
#     window.update()              # 창을 업데이트하여 변경 사항 반영
    
# # 파일 메뉴에서 '종료'를 선택하였을 때 호출되는 함수
# def quit():
#     window.quit()                # 창 종료
    
# def image_rotate():
#     global im,tk_img
#     out = im.rotate(45)
#     tk_img = ImageTk.PhotoImage(out)
#     canvas.create_image(250,250,image=tk_img)
#     window.update()
    
# def image_blur():
#     global im, tk_img
#     out = im.filter(ImageFilter.BLUR)
#     tk_img = ImageTk.PhotoImage(out)
#     canvas.create_image(250,250,image=tk_img)
#     window.update()
    
# window = tk.Tk()                 # tkinter 창 생성
# menubar = tk.Menu(window)        # 창에 메뉴바 생성
# canvas = tk.Canvas(window, width=500, height=500)  # 창에 500x500 크기 캔버스 생성
# canvas.pack()                    # 캔버스를 창에 배치

# filemenu = tk.Menu(menubar)      # 메뉴바에 파일 메뉴 생성
# filemenu.add_command(label='열기', command=open) # 파일 메뉴에 '열기'항목 추가, 이를 선택하면 open()함수 호출
# filemenu.add_command(label='종료', command=quit)
# filemenu.add_command(label='영상회전', command=image_rotate)
# filemenu.add_command(label='영상흐리게', command=image_blur)

# menubar.add_cascade(label='파일', menu=filemenu) # 메뉴바에 '파일' 레이블로 파일 메뉴를 추가

# window.config(menu=menubar)     # 창에 메뉴바를 설정
# window.mainloop()           # tkinter 창을 실행하고 이벤트 루프를 시작, 이 코드 이후부터 tkinter 창이 표시되고 사용자 입력 기다림

print('====================================================')

# img = Image.open('C:/doit/dog320.png')
# print(img.format, img.size, img.mode) # format, size, mode 확인
# img.show()

# box = (60,96,226,281) # 그림판에서 좌측 상단, 우측 하단 넣기
# crop_img = img.crop(box) # 이미지 자르기
# crop_img.save('june_torch.png') # 이미지 저장
# print(crop_img.format, crop_img.size, crop_img.mode) # format, size, mode 확인
# crop_img.show()

print('====================================================')

# 첫번째 예제
img = Image.open('C:/doit/liberty_of_statue.png')
print(img.format, img.size, img.mode)
# img.show()

box = (166,42,287,275)
(x1,y1,x2,y2) = box
w = x2-x1
h = y2-y1
crop_img = img.crop(box)
crop_img.save('crop_img.png')
print(crop_img.format, crop_img.size, crop_img.mode)
# crop_img.show()

a1 = 302
b1 = 49
a2 = a1+w
b2 = b1+h
drop = (a1,b1,a2,b2)
img.paste(crop_img, drop)
# img.show()

# 두번째 예제
c1 = 16; d1 = 193
img2 = Image.open('C:/doit/liberty_of_statue.png')
crop_img2 = crop_img.resize((40,90)) # 축소
drop = (c1, d1, c1+40, d1+90) # 이미지 붙이기 위치

img2.paste(crop_img2, drop) # 이미지 붙여 넣기

box = (166,42,266,142)
crop_img3 = img2.crop(box).rotate(90) # 회전
drop = (322,103,422,203) # 이미지 붙이기 위치

img2.paste(crop_img3, drop) # 이미지 붙여 넣기
img2.show()

# 세번째 예제
# from PIL import Image
# img4 = Image.open('C:/doit/liberty_of_statue.png')

# box = (182,44,274,272)
# crop4 = img4.crop(box) # 이미지 자르기
# crop_img4 = crop4.transpose(Image.FLIP_LEFT_RIGHT) # 자른 이미지 좌우 대칭
# drop = (280,48,372,276)
# img4.paste(crop_img4,drop)  # 이미지 붙여 넣기
# img4 = img4.transpose(Image.FLIP_LEFT_RIGHT) # 전체 이미지 좌우 대칭
# img4.save('C:/doit/liberty_of_statue.png')

# 세번째 예제
# img = Image.open('C:/doit/liberty_of_statue.png')
# img1 = img.filter(ImageFilter.CONTOUR) # 이미지 필터 CONTOUR
# img1.save('C:/doit/liberty_of_satue_CONTOUR.png')
# img2 = img.filter(ImageFilter.EMBOSS) # 이미지 필터 EMBOSS
# img2.save('C:/doit/liberty_of_statur_EMBOSS.png') 
# img3 = img.filter(ImageFilter.BLUR) # 이미지 필터 BLUR & SMOOTH_MORE
# img3 = img3.filter(ImageFilter.SMOOTH_MORE)
# img3.save('C:/doit/liberty_of_statue_BLURnSM.png')

# 네번째 예제
# split() 메소드로 RGB 칼라 평면 분리
# merge() 메소드에서 RGB 순서 바꾸어 합성
img4 = Image.open('C:/doit/liberty_of_statue.png')

rgb = img.split() # 이미지 칼라 분리하기
r,g,b = rgb[0], rgb[1], rgb[2]

img4 = Image.merge('RGB',(b,b,g)) # 이미지 칼라 합성하기
img4.save('C:/doit/liberty_of_statue_BBG.png')

img5 = Image.merge('RGB', (b,r,g)) # 이미지 칼라 합성하기

img5.save('C:/doit/liberty_of_statue_BRG.png')