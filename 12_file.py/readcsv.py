import csv # csv 모듈 임포트
import pprint

# movies.csv 파일 열기
with open('movies.csv') as file:
    # csv.reader() 함수는CSV 파일을 읽어들이는 읽기 객체를 반환함
    reader = csv.reader(file)   
    movies = list(reader)       # CSV 파일 내용을 리스트로 읽어들인다
    
# pprint.pprint(movies) # 읽어들인 내용을 화면에 출력 #pprint -> 데이터 구조를 보기 좋게 출력해 줌
# print(movies[1][0])  # Interstella

# title,genre,year
# Interstella,SF,2014
# Braveheart,Drama,1995
# Mary Poppins,Fantasy,1964
# Gloomy Sunday,Drama,2000

for i in range(1,5):
    for j in range(0,3):
        print(movies[i][j],end=',')
    print()
    
