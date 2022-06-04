#01

def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

# 02 
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i 
    return result

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

# 03

#input1 = int(input("첫번째 숫자를 입력하세요: "))
#nput2 = int(input("두번째 숫자를 입력하세요: "))

#total = input1 + input2 
#print("두 수의 합은 %s 입니다" % total)

# input 은 기본값이 문자열이라는 점을 기억하자 

# 04 
# print는 ,가 띄어쓰기를 의미한다 

#05 
f1 = open("test.txt",'w')
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

#06 
user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt','a',encoding = 'UTF-8') #encoding = 'UTF-8' 한글을 인식해주는 코드 
f.write(user_input)
f.write("\n")
f.close

#07 
f = open('test.txt', 'r')
body = "Life is too short \n you need java"
f.close()

body = body.replace("java", "python")
f = open('test.txt','w')
f.write(body)
f.close()