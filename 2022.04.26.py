#파이썬 총 복습 


# 자료형- 숫자형 
print(1)
a=3
b=4
print(a+b)

#제곱 표현 ** (a의 b제곱)
a=3 
b=4
print(a**b)

# 나머지와 몫 
print(7/3) # 나눗셈/
print(7%3) # 나머지%
print(7//3) # 몫// 

# 문자열 자료형 

food= 'python\'s favorite food is perl' # 따옴표의 기호 의미를 없애려면 앞에 백슬라이스를 넣어줘야 함 
print(food)

multiline= "life is too short\n you need python "  #줄 바꿈의 의미 
print(multiline)

multiline= """life is too short     
 you need python """                   #이게 더 편리한 줄바꿈이다
print(multiline)

head = "python"
tail= " is fun!"
print(head+tail)      # 문자열 더하기 

i= "python"
print(i*2)            #문자열 곱하기 

print("="*50)
print("my program")
print("="*50)        #문자열 곱하기 통해서 제목 만들기 

# 인덱싱 (가리킨다는 의미)

i= "hi, my name is Blair"
print(i[1])           # 파이썬은 0부터 숫자를 세는 것에 유의하자 
print(i[-1])          # -는 뒤에서부터 센다는 의미이다 
print(i[-0])          # -0 = 0

# 문자열 슬라이싱 ( 자른다는 의미이다)

i= "my favorite song is 0310"
print(i[0:9])
print(i[3:])     # 뒤에 문자를 쓰지 않으면 끝까지 출력된다
print(i[:9])
print(i[:])     # 이런 것도 가능 

mybirthday="19980621"
year=print(mybirthday[:4])  #주의해야할 점 끝번호는 슬라이싱에 포함하지 않음 (3까지만 슬라이싱 됨)
month=print(mybirthday[4:6])
day=print(mybirthday[6:])

#pithon을 python으로 바꾸기 
i="pithon"
print(i[0]+"y"+i[2:])

#문자열 포매팅 (문자열 안에 어떤 값을 삽입하는 방법)
i= "I like %d sushi" %3        # 숫자 삽입은 %d
print(i)
i= "I like %s sushi" %"five"    #문자 삽입은 %s
print(i)

i= " I have waited for %d days but I can't find who is %s" %(100,"subin")
print(i)                                                 # 2개 이상도 사용가능 

#주의 할점: ex) 98% 같은 %와 %d를 같이 쓰고 싶을 때는 %d%% 이런 식으로 두번 써줘야 한다. 


