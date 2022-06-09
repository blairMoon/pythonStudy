
import random 
random_num =random.randrange(100,999)
random_num_list = list(random_num)

strike = 0
ball = 0
while True:
    num = str(input())
    num_list = list(num)
    for i in random_num_list:
       if num_list[i] == random_num_list[i]:
           strike += 1 
       elif num_list[i] != random_num_list[i] and i in random_num_list:
           ball += 1 
    if strike == 3:
        break        
                    
    print(f'{strike} strike, {ball} ball')        

        