'''
#06 1부터 n까지 합을 출력하는 프로그램을 작성하시오
'''

total = 0
n = int(input("n= "))
for i in range(1, n+1): 
    total += i

print(total)