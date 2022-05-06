# 형태 
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

# bool 내장 함수 - 자료형의 참과 거짓 식별하기 
print(bool('python'))
print(bool(''))