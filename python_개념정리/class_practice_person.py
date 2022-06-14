# class 연습 
'''
1. Person class 를 정의하기
    - name, id, age, height, weight 변수선언
    - str(self) 메서드 재정의(overriding)
        - str 메서드 공부 및 관련 개념 찾아보기(모르면 스킵)
    - 각각의 age, height, weight 대입
    - 5명의 데이터를 생성하고 출력
'''

class Pesron_class:
    def person(self, name, id, age, height, weight):
        self.name = name
        self.id = id
        self.age = age
        self.height = height
        self.weight = weight
               
        
member1 = Pesron_class()
member1.person("오수빈","subbny", 25, 160, 45)
member2 = Pesron_class()
member2.person("가나다","abc", 24, 162, 47)
member3 = Pesron_class()
member3.person("마바사","erw", 35, 165, 40)
member4 = Pesron_class()
member4.person("아자차","qwre", 45, 155, 10)
member5 = Pesron_class()
member5.person("카타파","234", 34, 175, 90)        

print(member1.name)