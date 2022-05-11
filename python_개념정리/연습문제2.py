#01 
from re import I


a = "Life is too short, you need python."
if  'wife' in a : print('wife')
elif 'python' in a and "you" not in a: print("python")
elif 'shirt' not in a : print("shirt")
elif 'need' in a: print('need')
else: print("none")

## 참인 것들이 다 출력되는 것이 아니라 가장 먼저 참인 것만 출력되는 것이다. 

#02 
result = 0 
i = 1 
while i <= 1000:
    i += 1           # 뚯?
    if i % 3 == 0:
        result += i 
    
print(result)  

#03 

i = 0 
while True : 
    i += 1
    if i > 5 : break
    print("*" * i)

 #04

for i in range(1,101):
    print(i)   


#05 
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0 
for score in A:
    total += score
averge = total // 10  #len(A)
print(averge)    

#06 
number = [1,2,3,4,5]

result = []
for n in number:
    if n % 2 == 1:
        result.append(n*2)
print(result)    

