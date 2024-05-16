class Calculator: # 부모 클래스
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class Scientific_calculator(Calculator): # 자식 클래스
    pass

Scientific_1 = Scientific_calculator(6,6)
print(Scientific_1.mul()) # 36


