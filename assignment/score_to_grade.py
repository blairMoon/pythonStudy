'''
#05 시험 점수에 따른 등급을 출력하는 프로그램을 작성하시오. 
90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F
'''

score = int(input("그대의 점수는: " ))
if 90 <= score <=100 :
    print('A')
elif 80 <= score: 
    print('B') 
elif 70 <= score:
    print('C')     
elif 60 <= score:
    print('D')    
else:
    print('F')
