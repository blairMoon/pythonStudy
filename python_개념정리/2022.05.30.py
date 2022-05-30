# 함수 구조 예제 작성 
def add(a ,b):
    return a + b

print(add(2,3))   

a = 2
b = 3
c = add(2,3)
print(c)

# 일반적인 함수 
def add(a, b):
    result = a + b
    return result

a = add(3 ,4)
print(a)


# 입력값이 없는 함수 => 결과값을 받을 함수 = 함수이름()
def say():
    return 'HI'

a = say()
print(a)

# 결과값이 없는 함수 
def sum(a ,b):
    print("%d, %d의 합은 %d 입니다." % (a, b, a + b))

sum(1 ,2)

# 결과값이 없는 함수는 프린트를 하면 none이 출력되고, 함수를 쓰면 프린트 값이 출력된다 (append도 결과값이 없는 함수)

# 입력값도 결과값도 없는 함수 

def say():
    print('hi')

say()   

# 출력값 = hi

# 매개 변수 지정하여 호출하기 

def add(a ,b):
    return a + b

result = add(a = 3, b = 7)
print(result)    

# 매개 변수 지정하면 좋은 점 : 순서와 상관없이 사용 가능 

result = add(b = 5, a = 3)
print(result)

# 입력 값이 몇개가 될 지 모를 때는 *args 사용 

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1,2,3,4,5))


# **kwargs =-> 딕셔너리를 사용하고 싶을 때 사용  

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1) 
#{'a': 1}
print_kwargs(name = 'foo', age = 3)
#{'name': 'foo', 'age': 3}

# 함수의 결괏값은 언제나 하나이다. 
def add_and_mul(a, b):
    return a + b, a * b 

result = add_and_mul(3,4)
print(result)
#(7, 12) => 즉 튜플로 한 값만 나옴 
print(result[0])
# 7 => 이렇게 자리를 정해주면 둘 중 하나의 값만 나오게 설정할 수 있음 

#매개 변수의 초기값 미리 설정하기 
def say(name, old, man =True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
say("오수빈", 25)
'''
나의 이름은 오수빈입니다.
나이는 25살입니다.
남자입니다
'''

say("오수빈", 25, False)      
'''  
나의 이름은 오수빈입니다.
나이는 25살입니다.
여자입니다
'''

# 주의해야할 점 
'''
def say(name, man = False, old):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

#print("오수빈", 25)       

#SyntaxError: non-default argument follows default argument
'''
'''
초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정해 놓지 않은 매개변수는 사용할 수 없다. 
즉 컴퓨터가 25를 man과 old 중 어디에 넣어야 할지 알 수 없다는 것이다.
매개변수(man = False)를 맨 뒤에 놓아야한다.
'''

# 함수 안에서 선언한 변수의 효력 범위 

a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)    

# 1이 출력된다 
# why? 함수 안의 a는 오로지 함수 안에서 쓰이는 매개변수이기 때문에 프로그램이 인식하지 못한다. 

# 관련 예제 
def vartest(y):
    y = y + 1

vartest(3)
#print(y)    

# 오류가 난다. 그 이유는 y는 역시 함수안에서 사용된 변수이기 때문에 컴퓨터는 print 해야할 y변수를 찾지 못해서 
# 오류가 생기는 것이다. 


# 함수 안에서 함수 밖의 변수를 변경하는 방법 

# 1. return 사용하기 
a = 1 
def vartest(a):
    a = a + 1
    return a 

a = vartest(a)  # 여기서 함수 안의 a(return 해준 값)와 변수 a는 다른 것이다 
print(a)    

# 결과값: 2 

#2. global 명령어 사용하기 (별로 좋은 방법은 아님- 함수는 독립적으로 사용하는 것이 좋음)
a = 1 
def vartest():
    global a 
    a = a + 1

vartest()
print(a)

# lambda (def를 사용할 정도로 복잡하지 않거나, def를 사용할 수 없는 곳에 쓰임)
# 형태: lambda 매개변수1, 매개변수2 : 매개변수를 사용한 표현식
add = lambda a, b: a + b
result = add(3, 4)
print(result)




