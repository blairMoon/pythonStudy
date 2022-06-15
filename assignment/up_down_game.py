# up_down_game 
import random 

random_num = random.randrange(0,100)

while True:
    pick_num = int(input())
    if pick_num > random_num:
        print("dowm")
    elif pick_num < random_num:
        print("up")
    else:
        print("correct")
        break
