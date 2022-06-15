import random

random_num = str(random.randrange(100,999))
print(random_num)
while True:
    strike = 0
    ball = 0
    word = input()
    for i, ch in enumerate(word):
        if ch == random_num[i]:
            strike += 1 
        elif ch in random_num:
            ball += 1 
    print(f'{strike} strike, {ball} ball')

    if strike == 3:
        break
        

        