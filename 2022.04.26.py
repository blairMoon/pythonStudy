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

# 헷갈릴 수 있는 건 숫자형은 슬라이싱이나 인덱싱이 안된다. 무조건 문자열 자료형으로 바꿔줘야 한다!! 


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


# 포맷코드 숫자랑 사용하는 방법 
i="%10s" % "hi"
print(i)               #오른쪽 정렬하고 나머지 빈칸은 숫자만큼 비워둬 

i="%-10sjane" % "ho"
print(i)               #-니까 왼쪽 정렬하고 나머지 빈칸 비워둬 
                       # 이부분에서 헷갈렸던 건 블로그에 정리해뒀다 

#format 함수를 통해서 포매팅
i= "I eat {} apples".format(3)
print(i)                       
i= "I eat {} apples".format("five")  #문자로도 가능 
print(i) 

i= "I ate {} apples. so I was sick for {} days".format(3,"four")
print(i)                                # 2개이상 값 넣기 가능 

## 질문한 것들 
number=10
day="three"
s="I ate {0} apples. so I was sick for {1} days.".format(number,day)
print(s)
 #--> {}안에 숫자를 넣지 않아도 출력이 되는데 굳이 넣은 이유는 순서를 알려주는 것이다.
 # 0과 1를 바꿔서 넣으면 반대로 출력이 된다. 따라서 순서대로 출력하고 싶으면 생략해도 된다.

 #만약 여기서 굳이 변수를 설정하지 않고 바로 출력하고 싶다면? 밑과 같이 {}안에 바로 넣을 수도 있당
a="I ate {number} apples. so I was sick for {day}.".format(number=8,day=3)
print(a)


#포매팅 함수를 활용한 왼쪽 정렬 (hi를 화살표 방향으로 밀고 문자열은 10자리수로 만들어라)
a="{0:<10}".format("hi")
print(a)

#오른쪽 정렬 
a="{0:>10}".format("hi")
print(a)
#가운데 정렬 
a="{0:^10}".format("hi")
print(a)
# 공백 채우기 {0:이곳^10} '이곳'에 원하는 문자 넣어서 채울 수 있음 
a= "{0:=^10}".format("hi")
print(a)

# 소수점 표현하기 
y= 3.4543085304985039485943859485304985
a="{0:0.12f}".format(y)
print(a)

# {} --> 이거 문자로 표현하고 싶다면 두번쓰면 됨 
print("{{and}}".format())

print("{and}")

# f문자열 포매팅 (버전이 올라가면서 포매팅을 더 간단하게 표현 가능해짐)
name='홍길동'
age=30 
a=f'나의 이름은 {name}입니다. 나이는 {age+1}입니다'  #(+1같은 것도 가능하다)
print(a)

#딕셔너리에서는 이렇게 사용할 수 있다고 함 
d={'name':"오수빈",'age':25}
a=f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]} 입니다'
print(a)   #근데 뭔가 복잡해서 굳이 딕셔너리를 이렇게 사용해야하나 싶음 

#f문자열포매팅을 사용해서 '!!!python!!!' 문자열 출력해보기 
a=f'{"python":!^12}'
print(a)

#문자열의 내장 함수 a.count(a는 변수가 a라서 붙인거임) 
a='asdfasldkfheijiejf'
print(a.count('a'))

#위치 알려주는 함수 find --> 만약 존재하지 않은 문자열이면 -1을 반환함 
b= "python is the best choice"
print(b.find("t"))

#위치를 알려주는 함수 index --> 존재하지 않은 문자열이면 오류가 남 
b= "python is the best choice"
print(b.index('i'))

#문자열 삽입 join (""를 '23232'사이사이에 넣으라는 뜻)
b="".join('23232')
print(b)

# join함수를 리스트에 사용해보면 
l=",".join(["함수","모여","나도","몰라"])
print(l)     # 위처럼 나눠주기도하지만 리스트에서 합쳐주는 느낌으로 사용함 

# 소문자를 대문자로 바꾸고 대문자를 소문자로 바꾸기 
a='hi'
b='COCO'
print(a.upper()) 
print(b.lower())

# 왼쪽,오른쪽 공백 지우기 (strip 함수 사용)
a='    hi'
print(a.lstrip())
a='hi        '
print(a.rstrip())
# 이런 식으로 하고 양쪽 공백 지우는건 a.strip 쓰면 된다 

#문자열 바꾸기 (replace 함수 사용)
a= "my life is mine "
b=a.replace("life","love")
print(b)

# 문자열 나누기 (split함수 사용-문자열안에 있는 것으로 기준을 잡고 기준으로 나눠줌 )
a="I don't know what is my hobby."
print(a.split(" "))

a= "co3co3co3co3"
print(a.split("3"))