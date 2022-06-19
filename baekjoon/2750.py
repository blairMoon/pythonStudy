'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다.

이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

sort_list = []
N = int(input())
for _ in range(N):
    sort_list.append(int(input()))

for _ in range(N):  # for문을 쓸 때 항상 임시 변수 i가 들어가야 하는 것은 아니다 (i를 쓰지 않고 돌리고 싶다면 _사용)
    for j in range(N-1):
        if (sort_list[j]) > (sort_list[j+1]):
            (sort_list[j]), (sort_list[j+1]) = (sort_list[j+1]),  (sort_list[j])
           
sort_str = '\n'.join(map(str, sort_list))  # 이 식보다 for문 돌려서 출력하는 게 더 간편하다고 피드백 받음
print(sort_str)

#for n in sort_list:
#    print(n) 
        


'''
sort_list = []
count_N = int(input())
for i in range(count_N):
    N = int(input())
    sort_list.append(N)

for i in sort_list:
    for j in range(count_N):
        while i > sort_list[j]:
            sort_list[j - 1] = sort_list[j]
            sort_list[j] = i
           
print(sort_list)
'''        

