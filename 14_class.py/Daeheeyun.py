class Daeheeyun:
    class_value = 0
    
    def __init__(self):
        self.instance_value = 0
        
    def set_class_value(self):
        Daeheeyun.class_value = 10
        
    def set_instance_value(self):
        self.class_value = 20
    
instance1 = Daeheeyun()
instance2 = Daeheeyun()

print('-- 클래스 속성 변경 --')
instance1.set_class_value()
print(instance1.class_value, instance2.class_value) # 10 10

print('-- 인스턴스 속성 변경 --')
instance1.set_instance_value()
print(instance1.class_value, instance2.class_value) # 20 10

# 근데 웬만하면 이렇게 씀
print(Daeheeyun.class_value) # 10

print('-- 속성(Attribute) 출력 --')
print(instance1.__dict__) # {'instance_value': 0, 'class_value': 20}
print(instance2.__dict__) # {'instance_value': 0}