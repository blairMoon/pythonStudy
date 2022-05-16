'''
9개의 서로 다른 자연수가 주어질 때, 

이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
l = []
l = a,b,c,d,e,f,g,h,i
max_num = 0
for n in l:
    if max_num <= n:
        max_num = n 
print(max_num,l.index(max_num)+1)        


# 나만 이렇게 푼 거구나...9개를 한꺼번에 입력할 수 있는 코드가 있었구나... 
'''
numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)
'''    