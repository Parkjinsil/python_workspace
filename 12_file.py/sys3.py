# sys3.py
import sys ## 1)
if len(sys.argv) > 1: ## 2)
    filename = sys.argv[1]
    file = open(filename,'r',encoding='utf8') ## 3)
    text_str = file.read() ## 4)
    print(text_str)
    file.close() ## 5)
else:
    print('읽어들일 파일을 입력해주세요')
    
'''
1. 스크립트를 실행할 때 인자를 받기 위해서 sys 모듈이 필요
2. 실행 인자는 sys.argv 에 저장되어 있다. 이 리스트의 첫 인자는 스크립트 파일 이름이며, 그 이후부터가 전달된 인자
3. open() 함수를 이용해서 파일을 텍스트 읽기 모드로 엶 (파일 인코딩은 utf8)
4. 파일의 ㅇ전체 내용을 읽어서 text_str에 할당. 이 값은 문자열 타입
5. 파일의 내용을 출력한 후에 파일으 닫아줌
'''
        


