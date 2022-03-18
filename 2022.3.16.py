# 튜플과 리스트의 차이 (리스트는 추가및 변경 가능, 튜플은 변경 불가능 -잠겨 있단 생각)
# 튜플은 ()사용, 리스트는 []사용
t1=(1,2,'a','b')
# 슬라이싱, 인덱싱, 곱하기, 더하기 가능 
t2=(4,5)
print(t1+t2)
#튜플은 변하지 않는다는게 핵심 (더하기 곱하기를 해도 t1.t2는 여전하다)
a=(1,2)
a= a*3
print(a)

# 튜플끝? 어디에 쓰이는지는 잘모르겠다.. 하하 

"""
지금부터 dictionory 배울거에용~~~
자주 활용되는 개념이라 매우 중요해요 ~~~~
"""
dic={'name': "Blair", 'age': 25}

print(dic['name'])

a={1:'a'}
#쌍추가하는 방식 
a['name']="뚜니"
#삭제방식 
del a[1]
print(a)

# 딕셔너리의 핵심은 키와 밸류가 다르다는 것 
# 밸류를 통해 키를 얻을 수도 있고 키를 통해 밸류를 얻을 수도 있다 

dic = {'name':'subin','sex':"female",'age':'25','hobby': 'playing game'}
b=dic['name']
print(b)

# dic[]에 밸류를 넣으면 실행이 안된다 
#c=dic['subin']

# 키만 뽑기 
dic = {'name':'subin','sex':"female",'age':'25','hobby': 'playing game'}
b=dic.keys()
print(b)

# 밸류만 뽑기 
c=dic.values()
print(c)

# 쌍으로 얻기 
d=dic.items()
print(d)

#모두 지우기 
e=dic.clear()
print(e)

# dic.get을 쓰는 이유는 dic[]와 같은 결과값을 받지만  존재하지 않은 키를 입력했을 때 
#dic.get은 none의 결과를 도출하고, dic[]는 오류가 뜬다는 점이 다르다.
print(dic.get('job',"설명서에 없음"))




# 딕셔너리 자료형 주의점:키에 리스트를 쓸 수 없다, 키가 중복되면 안된다.

#키를 리스트로 만들기 
dic = {'name':'subin','sex':"female",'age':'25','hobby': 'playing game'}

# 해당 키가 딕셔너리안에 있는지 조사하기 
print('name' in dic)
print('job' in dic)
print('subin' in dic)
print("female" in dic)
# --> 밸류로 대입하면 무조건 false로 나오니까 key찾는데 쓰이는 것이 맞다. 


b=list(dic.keys())
print(b)
