#while문의 기본구조  (while + 조건문이 참이라면 계속적으로 반복함 )
treeHit= 0 
while treeHit < 10 :
    treeHit = treeHit +1 
    print ("나무가 {}번 찍었습니다".format(treeHit))
    if treeHit == 10:
        print("나무가 쓰러졌습니다") 


# while문 만들기 
prompt = """
1. ADD
2. DEL
3. LIST
4. QUIT

ENTER NUMBER:
"""
number = 0 
while number != 4:
    print (prompt)
    number = int(input())



   

# while문 강제로 빠져나가기 
coffee = 10 
money = 300 
while money :  #참일때 
    print ("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1   
    print (f"남은 커피의 양은{coffee}개 입니다. ")
    if coffee == 0:
        print ("오늘 영업 종료합니다")
        break

 # while문이 무한 반복될 때, 당황하지말고 터미널 클릭하고 ctrl+c누르면 멈춘다   
'''
 #coffee.py 
coffee = 10 
while True:
    money = int (input ('돈을 넣어 주세요: '))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee  - 1 
        print(f"남은 커피의 양은 {coffee}개 입니다.")
    elif money > 300:
        print(f'거스름 돈 {money-300 }를 주고 커피를 줍니다')
        coffee= coffee - 1 
        print(f"남은 커피의 양은 {coffee}개 입니다.")
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다")
        print(f"남은 커피의 양은 {coffee}개 입니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중단합니다.")
        break    
'''
# while문의 맨 앞으로 돌아가기 
a = 0
while a < 10 : 
    a = a + 1
    if a % 2 == 0 :
        continue
    print(a)

        
#1부터 10까지 숫자 중 3의 배수 빼고 나머지 값을 출력해보기 
a = 0 
while a < 10 :
    a = a + 1 
    if a % 3 == 0:
        continue
    else:
        print(a)    

        
