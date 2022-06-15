'''
직사각형의 정보를 저장할 클래스 Rectangle을 구현.
    - 클래스 이름: `Rectangle`
    - `생성자`
        - `Rectangle(width, height)`: 직사각형의 가로 길이를 `width`, 세로 길이를 `height` 설정한다. 
    - 멤버 함수
        - ` get_width() `: 직사각형의 가로 길이를 리턴한다.
        - ` get_height() `: 직사각형의 세로 길이를 리턴한다.
        - ` set_width(width)`: 직사각형의 가로 길이를 `width`로 변경한다. 만약, `width`가 0보다 작거나 같거나, 1,000보다 크면 변경하지 않는다.
        - ` set_height(height)`: 직사각형의 세로 길이를 `height`로 변경한다. 만약, `height`가 0보다 작거나 같거나, 2,000보다 크면 변경하지 않는다.
        - ` area() `: 직사각형의 넓이를 리턴한다.
        - ` perimeter() `: 직사각형의 둘레 길이를 리턴한다.
        - ` is_square() `: 정사각형이면 `true`, 아니면 `false`를 리턴한다.
'''

class Rectangle:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_width(self, w):
        return self.w		

    def get_hegiht(self, h):
        return self.h

    def set_width(self,w):
        self.w = w 

    def set_height(self, h):
        self.h = h

    def area(self):
        return self.h * self.w
		

    def perimeter(self):
        return (self.h + self.w) * 2
		

    def is_square(self):
        if self.h == self.w: 
            return True
        else:
            return False 


if __name__ == "__main__":
    rect = Rectangle(2, 5)   # 인스턴스 변수 지정 
    rect.set_width(100)   # 가로 길이 변경 
    assert 10 == rect.area()     # assert함수 이용해서 10인지 확인 
    assert False == rect.is_square()  # 정사각형 아닌지 확인 
    assert 14 == rect.perimeter()  # 둘레가 14인지 확인 




