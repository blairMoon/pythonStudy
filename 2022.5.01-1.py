a=[1,2,3]
print(a.clear())


# get 함수 이용하기 (get은 없는 값을 넣으면 none을 출력함 )
dic={'name':'subin','phone':'01027175527','birth':'19980621'}
print(dic.get('name'))

print(dic.get('soso'))

print(dic.get('too','mean'))
print(dic.get('too'))

'''
집합 자료형
'''
# 표현 
s1=set([1,2,3])   #리스트 위에 set을 씌워준다
print(s1)

# 특징 (중복을 허용하지 않고 순서가 없다)- 리스트,튜플과 다른점이다 
s1={1,2,3}
l1=list(s1)
print(l1)
t1=tuple(s1)
print(t1)

