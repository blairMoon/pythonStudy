a=[1,2,3]
print(a.clear())


# get 함수 이용하기 (get은 없는 값을 넣으면 none을 출력함 )
dic={'name':'subin','phone':'01027175527','birth':'19980621'}
print(dic.get('name'))

print(dic.get('soso'))

print(dic.get('too','mean'))
print(dic.get('too'))

print(dic.get('foo','bar'))


#해당 key가 딕셔너리 안에 있는지 조사하기 
dic={'name':'subin','phone':'01027175527','birth':'19980621'}
print('name' in dic)
print('subin' in dic)  # key가 있는지 조사하는 거지 value 조사를 하는 것은 아님 




'''
집합 자료형
'''
# 표현 
s1=set([1,2,3])   #리스트 위에 set을 씌워준다
print(s1)

# 특징 (중복을 허용하지 않고 순서가 없다)- 리스트,튜플과 다른점이다 
s1={1,2,3}
l1=list(s1)
print(l1)
t1=tuple(s1)
print(t1)

#교집합, 차집합, 합집합 
s1=set([1,2,3,4,5,6,7,8])
s2=set([4,5,6,7,8,9])
print(s1)
print(s2)
print(s1&s2) #교집합(&)
print(s1.intersection(s2))  #이것도 교집합 표현 

print(s1|s2)  # 합집합 표현 (|)
print(s1.union(s2))  #이것도 합집합 표현 

print(s1-s2)  #차집합 표현 
print(s2-s1)
print(s1.difference(s2)) # 이것도 차집합 표현 
print(s2.difference(s1))  

# 값 한개 추가하기 (add)
s1=set([1,2,3])
s1.add(4)
print(s1)

# 값 여러개 추가하기 (update)
s1=set([1,2,3])
s1.update([4,5,6])
print(s1)

#특정 값 제거하기 (remove)
s1={1,2,3}
s1.remove(2)
print(s1)

'''
불자료형
'''
# 정의 
a= True
b= False
print(type(a))
print(type(b))

# 조건문의 반환 값으로 사용되는 불 자료형 
print(1==1)  #==가 같다는 뜻이다 
print(2>1)
print(2<1)

#while문에서 실습 
a=[1,3,4,5]
while a:           #a가 참인동안 
    a.pop()        #리스트의 마지막 요소를 꺼낸다 
    print(a)       # 더이상 꺼낼 함수가 없다면 거짓이 되므로 중지된다!! 

# if문에서 실습 
if []: 
    print("참")
else:
    print("거짓")


if [1,2,3]:
    print("요기")
else: 
    print("조기")

#불 연산 (bool 내장함수 이용한 자료형의 참 거짓 판별)
print(bool("python"))
print(bool(''))
print(bool([1,2,3]))
print(bool("subin"))

'''
변수에 관하여
'''
a=[1,2,3]
b=a
print(id(a))
print(id(b))  #a와 b가 같은 주소를 가리키고 있는 것 

print(a is b)  #a와 b의 주소가 같은 지 물어보는 여부 

a[1]=4
print(b)  #a의 값을 바꿨는데 b도 같이 바뀐 이유는 둘이 같은 주소를 가리키고 있었기 때문이다 

# copy 사용 
from copy import copy
l=[3,4,5]
i=copy(l)
print(i)



# a와 같은 값인데 주소는 다르게 하고 싶다면? (복사하고 싶다면)
a=[1,2,3]
b=a[:]     # 이런 식으로 표현할 수 있다 
print(b)
print(id(a))
print(id(b))  
print(a is b)

# 변수 a와 b를 바꾸고 싶다면? (파이썬이 아닌 version)
a=3
b=4
tmp=b #tmp란 임시저장소 느낌?
b=a 
a=tmp
print(a)
print(b)    

# 파이썬 version 
a="hi"
b="bye"
a,b=b,a
print(a)
print(b)

#변수를 만드는 방법 
a,b='python','java'
print(a)
print(b)

(a,b)=('hi','bye')
print(a)
print(b)   #튜플이나 리스트 형태도 가능 

a=b='python'
print(id(a))
print(id(b))

# 간단 문제 
l=[1,2,3]
i=[1,2,3]
print(l is i) #어떤 결과가 나올까 : 다른 주소를 가리키고 있기 때문에 false가 나옴 





