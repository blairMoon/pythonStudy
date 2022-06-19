# 모듈 
# 함수나 변수 또는 클래스를 모아 놓은 파일 
# 1. 파일 불러 오기 (함수)
import mod2  # 파일 전체 불러오기 
print(mod2.add(3,4))  #mod2에 만들어 놓은 함수 불러오기 
# 결과값: 7 

from mod2 import sub # 파일에서 함수만 불러 오기 

print(sub(2,3))
# 결과값: -1 

from mod2 import*  # 파일의 모든 함수를 불러온다는 의미, *: 모든 것  

print(add(123,453))

#2. if __name__=="__main__": 의 의미 

#3. class 모듈 불러오기 
#  mod2에 있는 변수 불러오기 
print(mod2.PI)

# 변수값 활용해서 클래스 불러오기 
a = mod2.Math() #클래스 이름 앞에 모듈이름 입력 
print(a.solv(2))  # 원의 넓이 구하기

print(mod2.add(mod2.PI,4.4)) # 본 파일에 있는 변수 사용할 때도 앞에 파일명 꼭 붙이기 




    


