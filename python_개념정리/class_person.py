# class 연습 
'''
1. Person class 를 정의하기
    - name, id, age, height, weight 변수선언
    - str(self) 메서드 재정의(overriding)
        - str 메서드 공부 및 관련 개념 찾아보기(모르면 스킵)
    - 각각의 age, height, weight 대입
    - 5명의 데이터를 생성하고 출력
'''

class Person:
    def __init__(self, name, id, age, height, weight):
        self.name = name
        self.id = id
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return self.name 

    def info(self):
        return (self.age)

# people = []  
# while True:
#     name = input()
#     ...
#     weight = input()
#     people.append(Person(name, ..., weight))

#member1 = Person("오수빈","subbny", 25, 160, 45)
#print(member1)
#print(member1.info())