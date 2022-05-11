#01 
국어=80
영어=75
수학=55
print((국어+영어+수학)/3)

#02 짝수와 홀수는 보통 나머지를 통해 구분한다는 걸 기억하자아 
print(13%2)

#03
pin="881120-1068234"
yyyymmdd=print(pin[:6])
num=print(pin[7:])

#04
pin="881120-1068234"
print(pin[7])

#05
a="a:b:c:d"
a.replace(":","#")
print(a)

#06
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#07
a=["Life","is",'too',"short"]
result=" ".join(a)
print(result)

#08 
a=(1,2,3)
print(a+(4,))

#09 _list는 key가 될 수 없다  
a=dict()
print(a)

#10 
a={"A":90,'B':80,"C":70}
result=a.pop('B')
print(a)
print(result)

#11
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

#12 -변수 a와 변수 b가 같은 주소를 가리키고 있기 때문에 a에서 변화를 주면 b도 변화할 수 밖에 없다. 
a=b=[1,2,3]
a[1]=4
print(b)
