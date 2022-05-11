#1
국어=80
영어=75
수학=55
print((국어+영어+수학)/3)

#2
a=13%2 
print(a) 

#3,4
pin= "881120-1068234"
yymmdd=pin[:6]
num=pin[7:]
print(yymmdd)
print(num)
print(pin[7])


#5
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#6
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7
a = ["Life","is","too","short"] 
result= " ".join(["Life","is","too","short"])
print(result)