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
'''

#a ="123"
#print(a[::-1])

#a="I don't know what is my hobby."
#print(a.split(" "))


#a = "aaabbb"
#print(a.count("b"))
'''
word = str(input())
max_num = float('-inf')
for i in word:
   num = word.count(i)
   for i in word: 
       
   if max_num <= num:
    max_num = num   
    al = i

print(al)
'''

#   if a <= max_num:
#      a = max_num 
#print(max_num)


'''
a = [1,2,3]
print(a[2])
'''
'''
numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)
'''
'''
l = []
a = int(input()) % 5
l.append(a)
print(l)
'''
'''
def sum(a ,b):
    print("%d, %d의 합은 %d 입니다." % (a, b, a + b))

sum(1 ,2)
'''
'''
list = ["오수빈", 25, 35 ]
list2 = ['민병관', 22, 44]
list3 = ['박승아', 24, 42] 

list.sort
'''

n = '123'
print(n[0])