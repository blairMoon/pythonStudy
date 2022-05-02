#튜플정리 
# -튜플과 리스트의 가장 큰 차이점은 튜플은 값을 바꿀 수 없고 리스트는 값 변경이 가능하다는 점이다. 
# 값이 변경되지 않길 바랄 때 튜플을 사용하고 적은 메모리와 빠른 속도를 가진다는 장점이 있다. 

#튜플 형태 
from re import A
from turtle import clear


t1=(1,2,3)
t4=(1,3,4,(1,2,3))
t2=(5,) # 가장 중요한 거는 이렇게 한개의 값만 가질 때는 값 뒤에 콤마를 붙여야 한다는 것이다. 

#튜플 인덱싱
t=(5,6,7)
print(t[0])

#튜플 슬라이싱 
t=(5,6,7)
print(t[1:])

#튜플 더하기, 곱하기는 가능하다 
t=(5,6,7)
o=(1,2,3)
print(t+o)
print(t*4)

#튜플 길이 구하기 
t=(5,6,7)
print(len(t))

# 튜플 (1,2,3)에 값4를 추가하기 
t=(1,2,3)
t2=(4,)
print(t+t2)

"""
딕셔너리 자료형 (키를 통해 밸류를 얻는 자료형)
"""
# 딕셔너리 형태 

dic={'name':'subin','phone':'01027175527','birth':'19980621'}
print(dic['name'])

# 딕셔너리 쌍 추가하기 
dic={'name':'subin','phone':'01027175527','birth':'19980621'}
dic['address']='성남'
print(dic)
dic['리스트']=[2,4,5]
print(dic)  # 리스트도 추가 가능하다. 

# key를 통해 value를 얻기 (value를 통해 key를 얻을 순 없음)
dic={'name':'subin','phone':'01027175527','birth':'19980621'}
print(dic['birth'])

dic2={1:2,3:4}
print(dic2[1])  # 딕셔너리에서 1은 그냥 key 값이지 리스트나 튜플에서처럼 순서를 나타내는 1이 아님 

#딕셔너리 만들 때 주의 사항 
dic={1:'a',2:'b',1:2}
print(dic[1])  # key가 두개일 경우 앞의 키가 무시됨 

# + key에 리스트를 쓸 수 없지만 튜플은 가능하다 (변하는 값이 아니면 된다) value는 아무거나 상관없음 

# keys 함수 (키만 뽑기)
dic={'name':'subin','phone':'01027175527','birth':'19980621'}
print(dic.keys())
print(list(dic.keys()))  # key를 뽑은 걸 다시 리스트로 뽑기 

'''
자료형을 리스트로 만들 때 list()

a=(1,2,3)
print(list(a))

'''

# values (밸류만 뽑기)
dic={'name':'subin','phone':'01027175527','birth':'19980621'}
print(dic.values())
print(list(dic.values()))

# items (key,value 쌍으로 얻기)
print(dic.items())
print(list(dic.items())

#clear (쌍 모두 지우기)
a={'name':'subin','phone':'01027175527','birth':'19980621'}
a.clear()
print(a)
#get(key로 value 얻기)
dic={'name':'subin','phone':'01027175527','birth':'19980621'}
