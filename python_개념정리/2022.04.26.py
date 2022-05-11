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
l=",".join(["함수","모여","나도","몰라"])  # 무슨 뜻이냐 각각 사이에 ','를 넣되, 문자열로 만들어달라! 
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

# 리스트 자료형 (방대한 데이터를 효율적으로 관리하기 위한 자료형의 일종)
#- 변수가 늘어나면 관리가 어렵기 때문에 각각의 변수를 하나의 변수에서 관리할 수 있는 것? 
리스트명=["요소1","요소2","요소3"] 

#리스트도 인덱싱 가능 
list=[1,2,3]
print(list[0])
print(list[0]+list[2])  # 더하기도 가능 
print(list[-1])  # -1은 뒤에서 1번 

#리스트 안에 리스트 존재하는 것도 가능 
list=[1,2,3,['d','c','e']]
print(list[3])
print(list[3][0]) #리스트 안의 리스트에서 값을 출력하는 방법 

#리스트 슬라이싱 
list=[1,2,3,4,5]
print(list[0:2])    # [이상:미만]인 것을 기억하자 

a=[1,2,3,4,5]
print(a[1:3])

# 리스트 더하기 
l=[1,2,3,4,5]
s=[7,8,3,0]
print(l+s)    #문자가 중복되어도 삭제하지 않는다 

#리스트 반복하기 
l=[12,3,213]
print(l*3)

# 리스트 길이 구하기 (len함수 사용)
l=[12,4,5,6,7,4,5,6]
print(len(l))

# 추가 함수 (str함수 )
a=[1,2,3] 
print(str(a[2])+"hi")  #a[2] 즉 3과 hi를 더하고 싶은데 그냥 더하면 숫자와 문자형의 덧셈은 오류가 나므로 str함수를 써야한다.

# 리스트 수정 (따로 함수 x)
l=[1,2,3]
l[2]=0    # 그냥 바꿔주기만 해도 수정 가능하다(따로 함수를 씌우지 않아도)
print(l)

#리스트 삭제 (del 함수)
l=[1,2,3]
del l[1]
print(l)

# 리스트에 요소 추가하는 함수 (append)
a=[1,2,3]
a.append(5)
print(a)

a.append([6,7])
print(a)        #리스트에 리스트를 추가할 수도 있다. 

# 리스트를 정렬해주는 함수 (sort) (알파벳 순서나, 숫자를 순서대로 )
a=[1,4,5,3,4,5]
a.sort()
print(a)

a=['사과','과자','파인애플']
a.sort()
print(a)    # 가나다라 순으로 정렬해줌 

#리스트 뒤집기 (reverse)
a=[1,3,4]
a.reverse()
print(a)    # 그냥 현재 리스트에서 반대로 나열하는 것이다.(알파벳 순서 반대나, 일반 순열을 반대로 하는게 아님) 

#위치 반환 (index)
a = [3,4,5]
print(a.index(3))

#리스트에 삽입하기 (insert)- insert와 append 구분하기 
l=[3,4,5]
l.insert(0,1)
print(l)

#추가로 extend라는 함수도 있는데 이건 iterable 자료형만 삽입가능한 함수라고 한다 
l=[3,4,5]
l.extend([7,8])
print(l)

# 리스트 요소 제거(remove함수)
a=[1,2,3,4,5,6,3]
a.remove(3)
print(a)     # 3이 두개 있을 경우 첫번째 값만 삭제됨 

#리스트 요소 끄집어내기 (pop함수)
a=[1,2,3]
print(a.pop(2))   # 이렇게 print안에 pop함수를 쓰면 x번째 요소를 끄집어낸다 
print(a)   # 그리고 a를 다시 출력해보면 삭제된 걸 알 수 있다. (이걸로 뭔가 추첨 프로그램에 활용하기 좋을 것 같다)

a=[5,6,7,23]
print(a.pop())  # 이렇게 괄호안에 아무 값도 쓰지 않으면 가장 마지막 값을 끄집어 내구 
print(a)   #  삭제한다!

#요소의 개수 세기 (count함수)
l=[3,4,5,5,5,6,6,7]
print(l.count(5))



