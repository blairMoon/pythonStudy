
import random 
random_num =str(random.randrange(100,999))
random_num_list = list(random_num)

strike = 0
ball = 0
while True:
    num = str(input())
  
    for i in random_num_list:
       if num[i] == random_num_list[i]:
           strike += 1 
       elif num[i] != random_num_list[i] and i in random_num_list:
           ball += 1 
    if strike == 3:
        break        
                    
    print(f'{strike} strike, {ball} ball')        

        