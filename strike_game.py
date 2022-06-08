
import random 
random_num = str(random.randrange(100,999))
num = str(input())

strike = 0
ball = 0
while True:
    for i in num:
        for j in random_num:
            if int(num[i]) == int(random_num[j]):
              strike += 1
            elif i in random_num:
                ball += 1
    if strike == 3:
        break
                
    print(f'{strike} strike, {ball} ball')        

        