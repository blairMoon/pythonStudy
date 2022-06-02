'''
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

'''
N = int(input())
sosu = []
for i in range(N + 1):
   if i % 2 == 0 and i != 2:
        notsosu = i
   elif i == 1:
       notsosu = i   
   elif i % 3 == 0 and i != 3:
        notsosu = i
   elif i % 5 == 0 and i != 5:
        notsosu = i
   elif i % 7 == 0 and i != 7:
        notsosu = i
   else:
        sosu.append(i)  
soinsu = [ ]
while True:
    for i in sosu:
        if N % i == 0:
            soinsu.append(i)
            N // i
        elif N == 0:
            break
    print(soinsu)                