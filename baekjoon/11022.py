'''

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. 

x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

'''
T = int(input())
x = 0
for i in range(T):
    A, B = map(int, input().split())
    x += 1
    C = A + B
    print(f"Case #{x}: {A} + {B} = {C}")    
    
# 혼자 해결 


# 더 짧은 코드 
'''
 t = int(input())

for x in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{x}: {a} + {b} = {a+b}')
'''  
