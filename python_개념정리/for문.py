#for문 기본 형식
test_list = ['one', 'two', 'three' ]
for i in test_list:  #i=임의 변수 , test_list에는 튜플, 문자열 , 리스트 , range함수 등 가능 
    print(i)

#다양한 for문 사용 
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)    

# 튜플 기능 중 (a,b) = (1,2) 활용 

# for문의 응용 
number = 0 
marks = [90, 25, 67 , 45, 80] 
for mark in marks:
    number = number + 1 
    if mark > 60:
        print(f'{number}번 학생은 합격입니다. 축하드려요')
    else:
        print(f'{number}번 학생은 불합격입니다. 다음 기회를 노려보세요.')        
# continue 사용 
number = 0 
marks = [90, 25, 67 , 45, 80] 
for mark in marks:
    number = number + 1 
    if mark < 60:
        continue
    else:
          print(f'{number}번 학생은 합격입니다. 축하드려요')


# range 함수 (시작 숫자(이상),끝 숫자(미만))
a = range(10) == range(0,10)
print(a)   

#range 함수 사용한 for문 예시 
# 1번째 version
add = 0 
for i in range (1, 11):
    add = add + 1


print(add)

''' 
먼저 add = add + 1 에 대해서 
i를 썼어야 했는데 실수로 1를 넣었다. 
그런데 출력값이 10이 나와서 당황했다. 
add는 range함수로 범위를 정해주지 않았는데 왜 10이라는 값이 나왔을까 ... 
답은 일단 for문 자체에 range(1,11)이 걸려서 10번 add와 상관없이 10번 실행하는 것이었다. 


'''

# 2번째 version (1~10까지 더하기 )
add = 0 
for i in range (1, 11):
    add = add + i


print(add)

'''
add = add + i 를 바로 해석할 수 없어서 계속 직접 작성해봤는데 
그냥 더한 값에 다음 숫자 계속 더해주기라고 단순하게 생각하면 될 것 같다. 

'''


# 3번째 version 

marks = [90, 23, 45, 60, 70]
for number in range(len(marks)):
    if marks[number] < 60: continue
    else:
        print(f"{number} 학생 추카포카")

# for문과 range함수를 사용하여 1부터 100까지 더해보자 
add=0
for i in range(1,101):
    add = add + i 

print(add)

# print의 위치가 어디있느냐에 따라서 5050만 출력되는지 과정 전체가 출력되는지가 나뉜다. 
# for문 안에 print가 포함되어 있으면 과정 전체가 출력되고, for문에 포함되어 있지 않으면 마지막 결과값만 출력된다.

# for와 range를 사용한 구구단 (이중 for문)  
     
for i in range(1,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print(" ") 

# 마지막에 print("")을 하는 이유는 i -> j 순서로 돌아가다가 마지막에 print를 해줘야 끊김이 생기기 때문이다 
# 그렇지 않으면 줄줄이 안 끊기고 계속 프린트해서 가독성이 별로다.

# 리스트 내포 사용하기 (일단 급한거 아니므로 다음에 학습)
a= [1, 2, 3 ,4]