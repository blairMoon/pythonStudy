# 파일 읽고 쓰기 정리 

# 1. 파일 생성하기 

f = open("new_pile.txt", 'w')
f.close()

# 파일 객체 = open(파일 이름, 파일 열기 모드)

# 파일 열기 모드 
# r (읽기모드): 파일을 읽기만 할때 사용
# w (쓰기 모드): 파일에 내용을 쓸 때 사용 (원래 내용 모두 사라지고 새로)
# a (추가 모드): 파일의 마지막에 새로운 내용을 추가할 때 사용 

# 만약 새 파일을 C:\jocoing에 생성하고 싶다면, 
#f = open("C:\jocoding",'w')
#f.close()

# 파일을 쓰기 모드로 열어 출력값 적기 
f = open('C:\jocoding\ new_pile.txt','w')
for i in range(1, 11):
    data = '%d번째 줄입니다. \n' % i 
    f.write(data)
f.close

# realine 함수 사용하기 
# 첫번째 줄을 읽어 출력하는 함수 
'''
f = open("C:\jocoding\ new_pile.txt", 'r')
line = f.readline()
print(line)
f.close
'''
# readline 함수로 모든 줄을 읽고 싶을 때 
'''
f = open("C:\jocoding\ new_pile.txt", 'r')
while True:
    line = f.readline()
    print(line)
    if not line: break   # 
f.close()    
'''
# if not line 은 더이상 읽을 줄이 없다는 뜻이며 이때는 none을 출력한다.

# readlines 함수 사용하기 (줄의 요소를 리스트로 돌려주는 함수)

f = open("C:\jocoding\ new_pile.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# end = ''의 의미는 print 자체가 한칸 띄워서 프린트 해주는데 한 칸 붙이라는 의미이다. 

# read 함수 사용하기 (내용 전체를 문자열로 돌려주는 함수)

f = open("C:\jocoding\ new_pile.txt", 'r')
data = f.read()
print(data)
f.close()

# 함수에 새로운 내용 추가하기 
'''
f = open("C:\jocoding\ new_pile.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다. \n" % i 
    f.write(data)
f.close()   
'''
'''
# with문과 함께 사용하기 (close 안해도 되는 방법)
#정석 방법
f = open ("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()
# with 사용 방법 
with open("foo.txt",'w') as f:
    f.write('Life is too short, you need python')
'''

