'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

입력의 마지막에는 0 두 개가 들어온다.

각 테스트 케이스마다 A+B를 출력한다

'''

while True:
    A ,B = map(int, input().split())
    if A == 0 and B ==0:
        break
    else:
        print(A + B)



'''
# 틀린 코드 
while True:
    A ,B = map(int, input().split())
    print(A + B)
    if A == 0 and B ==0:
        break    

a와 b는 각각 1이상입니다. 
a와 b를 입력 받고, 두 수가 0이면 그 즉시 종료되어야 하는데
밑의 코드는 a와 b를 더해주고 0인지 확인하고 있네요.
'''
                 
    
    




#for i in range(T):
#    A ,B = map(int, input().split())
#    print(A + B)  
#else:
#    print('0','0')    