
import random 
random_num =str(random.randrange(100,999))
random_num_list = list(random_num)
random_num_list_str = ''.join(map(str,random_num_list))


while True:
    strike = 0
    ball = 0
    num = str(input())
    num_list = list(num)
    num_list_str = ''.join(map(str,num_list))
    for i in range(len(random_num_list)):
       if num_list_str[i] == random_num_list_str[i]:
           strike += 1 
       elif random_num_list_str[i] in num_list_str:
           ball += 1 
    print(f'{strike} strike, {ball} ball')

    if strike == 3:
        break
        

        