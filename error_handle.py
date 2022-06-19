# error 처리하기 
'''
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다") 
except IndexError:
    print("인덱싱할 수 없습니다")  
'''
# 출력값 : 인덱싱할 수 없습니다 (인덱싱 에러가 먼저 발생되었기 때문)
'''
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e) 
except IndexError as e:
    print(e)  
# 출력값: list index out of range (why??)
'''
# 두가지 에러 한꺼번에 처리하기 
'''
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)    
'''
# 출력값: list index out of range (이렇게 출력되는게 맞나?)

# 오류 회피하기  
from re import L


try: 
    f = open("나 없는 파일", "r")
except FileNotFoundError:
    pass

# 혼자 오류 예외처리 해보기 
try: 
    f = open("나 없는 파일", "r")
except FileNotFoundError:
    print("여기 있는 파일도 아닌데 왜 실행시켜 바보니?")

# 오류 일부러 발생시키기 
# ex) Bird 클래스를 상속받는 자식 클래스가 반드시 fly 함수를 구현하도록 만들고 싶은 경우 
class Bird:
    def fly(self): # fly를 사용하지 않으면 오류를 발생시켜라 
        raise NotImplementedError #파이썬 내장오류 - 꼭 작성해야하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용
#class Eagle(Bird):
#    pass  # fly를 사용하지 않음 

#eagle = Eagle()
#eagle.fly()

# NotImplementedError 오류가 발생되지 않게 하려면 
class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
eagle.fly()

# 예외 만들기 
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
'''
say_nick("천사")  
say_nick("바보")  
'''
# 천사는 그냥 출력되고 바보면 에러 출력하라는 함수로 인해 


try: 
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다")


# 오류메세지를 사용하고 싶다면 
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)






