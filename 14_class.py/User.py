class User:
    # Attributes or properties or variables
    phoneNumber = ''
    emailAddress = ''
    name = ''
    
    '''
    self 란?
    - 인스턴스 자체를 참조
      : self는 해당 메서드가 호출된 특정 인스턴스 객체 자신을 가리킴
        메서드 내에서 인스턴스의 속성(attributees)에 접근하거나 수정할 때 self 사용
    - 인스턴스 메서드 정의
      : 파이썬에서 인스턴스 메서드는 첫 번째 매개변수로 self 포함해야 함
        이는 메서드가 어떤 인스턴스에 대해 호출되었는지 알려주는 규약
    - 메서드 호출 시 자동 전달
      : 인스턴스 메서드를 호출할 때, 파이썬 인터프리터가 자동으로 해당 인스턴스를 self에 전달
        개발자는 명시적으로 self를 지정할 필요 X
    '''
    
    # 생성자 contructor
    def __init__(self, phoneNumber, emailAddress, name): # 받아온 매개변수 self 객체에 담아줌
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.name = name
    
    def getPhoneNumber(self): # 매개변수에 아무것도 안 넣어도 자동으로 아까 값 담은 self 넣어줌
        return self.phoneNumber
    
    def getEmail(self):
        return self.emailAddress
    
    def getName(self):
        return self.name
    
# user1 = User()
# user1.init('010-1234-5678', 'engineerk@endineerk.com','EngineerK')
# 원래 이렇게 써야하는데 init함수를 __init__으로 만들면 아래와 같이 한번에 만들 수 있음
user1 = User('010-1234-5678', 'engineerk@endineerk.com','EngineerK')

print(user1.getPhoneNumber())
print(user1.getEmail())
print(user1.getName())    

user2 = User('010-1111-2222','wlstlf971017@naver.com','Engineer')
print(user2.getPhoneNumber())
print(user2.getEmail())
print(user2.getName())    
