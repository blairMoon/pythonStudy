'''

#01. 다음과 같이 출력을 하시오. (단, for 사용)


*****
****
***
**
*
'''
#01
for i in reversed(range (0,6)):
    print (("*"*i))


#02
for i in (range (5,0,-1)):
    print (("*"*i))

'''



#02 다음과 같이 출력을 하시오. (단, for 사용). Hint: 스페이스바로 공백 표현

 * # '    *': ' '*4 + '*'
   ** 
  ***
 ****
*****

'''

for i in range(0,6):
    print("{0:>5}".format("*"*i))
      



'''
#03 다음과 같이 출력을 하시오. (단, for 사용)

    *
   ***
  *****
 *******
*********

''' 

for i in [1 ,3, 5, 7, 9]:
    print("{0:^10}" .format ("*" * i) )


'''

#04 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오. 

- A가 B보다 큰 경우에는 '`>`'를 출력한다.
- A가 B보다 작은 경우에는 '`<`'를 출력한다.
- A와 B가 같은 경우에는 '`==`'를 출력한다.  

'''
'''
A = int(input("A의 값은: "))
B = int(input("B의 값은: "))
if A > B: 
    print("`>`")
elif A < B:
    print("`<`") 
else: 
    print("`==`")       
'''
'''


#05 시험 점수에 따른 등급을 출력하는 프로그램을 작성하시오. 
90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F
'''
'''
score = int (input("그대의 점수는: " ))
if score >= 90:
    print('A')
elif 80 <= score < 90: 
    print('B') 
elif 70 <= score < 80:
    print('C')     
elif 60 <= score < 70:
    print('D')    
else:
    print('F')
'''

'''
#06 1부터 n까지 합을 출력하는 프로그램을 작성하시오
'''
'''
add=0
n = int(input("n= "))
for i in range (1,n+1): 
    add = add + i

print(add)
'''
'''
#07 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''
'''
N = int(input("N = "))
for i in range (1, N+1):
     N = N + 1
     print(i)
'''
'''
#08 N개의 정수가 들어 있는 리스트를 정의하고, 최솟값과 최댓값을 출력하는 프로그램을 작성하시오.
'''
#01
nums = [20, 10, 35, 30, 7]
nums.sort()
print(nums[0],nums[4])

#02
print(max(nums))
print(min(nums))

'''
#09 9개의 서로 다른 자연수가 있는 리스트를 정의하고,
 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오. 
 예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61 가 리스트에 들어 있으면, 
 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
 '''
 #01
nums = [3, 29, 38, 12, 57, 74, 40, 85, 61]
nums.sort()
print(nums[8])
print(nums.index(85))
#02 
nums = [3, 29, 38, 12, 57, 74, 40, 85, 61]
print(max(nums))
print(nums.index(max(nums)))
'''
#10 문자열 S를 정의하고, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
 S에는 QR Code "alphanumeric" 문자만 들어있다. 
 QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
'''
R = 0
S = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"



