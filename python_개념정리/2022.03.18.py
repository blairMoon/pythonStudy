#불 개념 개념 테스트 
print(1==1)

print('1')
print(1<2)


# 변수 개념 예제 
a= [1,2,3]
b = a  # a와 b가 같다는 뜻이 아니라 같은 곳을 바라보고 있다 (같은 주소를 가르키고 있다)
a[1]=4
print(id(a))
print(id(b))
print(a is b)

"""
변수 개념 !!! 


"""
# 특히 리스트 복사 
a = [1,2,3]
b = a  # a의 리스트를 복사한 새로운 리스트가 아니라 그저 같은 곳을 바라보고 있다 (같은 주소를 가르키고 있다)
a[1]=4
print(a)
print(b) # 둘이 같은 곳을 바라보고 있으니 같은 결과값이 나올 수 밖에 없다 

#둘의 아이디 주소도 같다 
print(id(a))
print(id(b))
print(a is b)

# 그렇다면 a와 같은 내용을 가진 new b를 만들어 내고 싶을 때 (복사하고 싶을 때) 어떻게 할까 
# 1. [:] 이거 활용하기 
a=[1,2,3,4,5,6,7]
b=a[:]
print(a)
print(b)
print(id(a))
print(id(b))

# 2. copy 활용하기 
from copy import copy
a= [1,2,4]
b= print(copy(a))
print(id(a))
print(id(b))
print(b is a)  #False로 나오겟지?? 

# 변수를 만드는 여러가지 방법 알아bogi 

#1. 튜플 사용한 변수만드는 방법 

a,b=('hell','house')
print(a,b)

#2. 리스트를 통해서 변수만드는 방법 

[a,b]=['python','Java']
print(a,b)
a=b='subin'
print(a,b)

# 두 변수의 값을 간단하게 바꿀 수 있는 방법 

a=4
b=2
a,b=b,a
print(a,b)



