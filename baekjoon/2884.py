'''

바로 "45분 일찍 알람 설정하기"이다.

이 방법은 단순하다.
 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 

현재 상근이가 설정한 알람 시각이 주어졌을 때,
 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
 '''

a, b = map(int , input().split())

if a>0 and b < 45:
    print(a - 1, b + 15)
elif b >= 45:
    print(a, b - 45)
else:
    print(23,b + 15)    



 # 틀린 코드 
a, b = map(int , input().split())

if a != 0 and b < 45:
    print(a - 1, b + 15)
elif a != 0 and b >= 45:
    print(a, b - 45)
elif a == 0 and b < 45:
    print(23 ,b + 15)
else:
    print(23,b - 45)    

# 불필요한 식이 많았던 것 같다.     