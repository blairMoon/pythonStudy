'''

#01. 다음과 같이 출력을 하시오. (단, for 사용)


*****
****
***
**
*
'''
#01
for i in reversed(range(0,6)):
    print("*"*i)


#02
for i in range(5,0,-1):
    print("*"*i)

#03
for i in range(5):
    print((5-i)*'*')
