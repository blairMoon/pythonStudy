# 클래스 
# 사칙연산 클래스 
class FourCal:
    def setdata(self, first, second):
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
    def div(self):
        result = self.first / self.second 
        return result     
a = FourCal()
a.setdata(4, 2)
print(a.add())


# 생성자 (초깃값 설정하기)

class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second 
    def setdata(self, first, second):
       self.first = first 
       self.second = second     