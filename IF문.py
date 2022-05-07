# 형태 
from pickletools import stackslice


money= True 
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

### 조건문에서 들여쓰기를 주의해야 한다. 

# if 조건문: 참과 거짓을 판별하는 문장 
# 불자료형, 비교연산자 등이 올 수 있다. 

a=[1, 2, 3, 4]
while a:
    print(a.pop())

if []:
    print('참')
else:
    print ("거짓")     

if [1, 2, 3]:
    print ("참")
else: 
    print ("거짓")     


# 내가 만들고 싶은 조건문 
## 바나나가 노랑색이면 진실을, 빨강색이면 거짓을 출력해라 

yellow= True
red=False
if yellow:
     print("banana is yellow")
elif red:
     print("banana is not red") 
### 이게 최선일깡 ,,,,,, 


banana_color = 'yellow'
if banana_color == 'red':
  print('false')
elif banana_color == 'yellow':
  print('true')

# bool 내장 함수 - 자료형의 참과 거짓 식별하기 
print(bool('python'))
print(bool(''))
print(bool([]))
print(bool(0))
print(bool(3))

#and,or,not 

#and -> x와 y 모두 참이어야 참이다 

money=2000

card=True
if money >= 3000 and card:
    print ("택시를 타고 가라")
else:
    print ("걸어가라")

# card는 참이었으나, money가 거짓임으로 "걸어가라"가 출력된다. 
money=4000

card=True  

if money >= 3000 and card:
    print ("택시를 타고 가라")
else:    
    print("걸어가라")

# card와 money가 모두 참이므로 "택시를 타고 가라"가 출력된다. 

# x in s, x not in s (파이썬에만 존재하는 조건문)
# 튜플과 문자열, 리스트에서 가능하다 
l=[1,2,3,4]

if 1 in l:
    print("1 in l")
else:
    print("1 not in l")     

 # 활용하여 다른 예제를 만들어 보면 

wallet=['credit card', 'money', 'name card']

if 'credit card' or 'money' in wallet:
    print ("밥을 먹어라")

else:
    print("굶어라")

#elif 활용하기 

#주의할 점 : if문이 거짓일 때, elif문이 실행되고, elif문이 거짓일 경우, else문이 실행된다. 

restaurant ='snacks','banana','sushi'
if 'pasta' in restaurant :

    print ("주문해라")

elif 'water' in restaurant:

    print ("그냥 나와라")

else:
    print ("아무거나 먹어라")

# else는 최후의 수단이고 어떠한 조건문이 붙지 않는다 


#if문을 한줄로 작성하는 방법 
if 'money'in restaurant: pass
else:print("도망쳐라")

# 조건부 표현식 
# print()--> 조건문이 참인경우 , if ~~ (조건문), else, print()--> 조건문이 거짓인 경우 

print("아무거나 먹어라") if 'money' in restaurant else print("나와라") 




