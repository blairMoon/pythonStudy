# 집합 기본형 
from re import A
from winreg import HKEY_LOCAL_MACHINE


s1 = set([1,2,3])
print(s1)
#집합 간단표현 
s2 = {1,2,3,4}
print(s2)
#집합을 리스트로 바꾸기 
s1= set([1,2,3])
l1=list(s1)
print(l1)
#집합을 튜플로 바꾸기 
s1= set([1,2,3])
t1= tuple(s1)
print(t1)
#교집합 (2가지 방법)
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8,9}
print(s1&s2)
print(s1.intersection(s2))
#합집합 (2가지 방법)
print(s1|s2)
print(s1.union(s2))
#차집합 
print(s1-s2)
print(s2-s1)
# 수학이랑 다른 점은 공통된 부분을 알아서 걸러준다는 것이다 

# 집합 자료형에 값을 추가하는 함수( 오직 한 값만 추가할 수 있다.)
s3={1,3,4}
s3.add(2)
print(s3)

# 집합 자료형에 값을 추가하는 함수( 여러개 값 추가하기)
s4=set("미진")
s4.update("유아","코리")
print(s4)

#특정 값 제거 
s3={1,3,4}
s3.remove(3)
print(s3)


l1=[1,2,3,3,4,4,4,5,5,5,6,6,6,7,7]
s1=set(l1)
print(s1)
L1=list(s1)
print(L1)

#불 자료형 
a=True
b=False
print([type(a)])
print([type(b)])

print(1==1)
print(2>1)
print(2<1)

a=[1,2,3,4]
while a:
  print(a.pop())

if[1,2,3]:
    print("참")
else:
    print("거짓")    

a=bool('python')    
print(a)
b=bool("")
print(b)

print(1==1)