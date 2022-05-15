'''
from tkinter import N


print(",".join('abcd'))
print("abcd".join(''))
print("abcd".join(''))

string=['s','u','b','i','n']
print("".join(string))

a=1.2,3,4,5
b="사과",'배','파인애플'
b=["사과",'배','파인애플']
print(b)


add = 0 
for i in range (1, 11):
    add = add + 1


print(add)

N = int(input())
count = 0
while 1:
    a = N // 10 
    b = N % 10
    a + (11 * b)
    count += 1
    if (a +(11 * b)) == N:
        break 
    print(count)
'''
N = int(input( ))
count = 0
a = N // 10 
b = N % 10
while 1:
    if 10 * b + ((a + b) % 10) != N:
        count += 1
    else:
        break
print(count)

