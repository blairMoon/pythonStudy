"""
    Print, Operator
    Version : 1.0
    Created : 2022. 3.17
    Updated : 2022. 3.17
    Author  : J.W.Lee
"""



# 1. 화면에 Hello + 본인이름을 출력하시오.
print("Hello J.W.Lee")

# 2. Mary's cosmetics
print('Mary\'s cosmetics')
print("Mary's cosmetics")

# 3. 신씨가 "도둑이야"라고 소리쳤다.
print('신씨가 "도둑이야"라고 소리쳤다.')
print("신씨가 \"도둑이야\"라고 소리쳤다.")

# 4. "C:\Windows"
print('"C:\\Windows"')

# 5. a = 'first', b = 'second'일 때 first second를 출력
a = 'first'
b = 'second'
print(a, b)


# a = input()
# print(a)
# b = input('값을 입력하든가 : ')
# print(b)
# c = float(a) + int(b)           # C나 Java는 (float)a, (int)b로 쓴다.
# print(c)
#
# # Special
# a, b = input('두 개 입력하든가 : ').split(',')
# c = float(a) + int(b)
# print(c)
#
# dd = []
# dd = input('두 개 입력하든가 : ').split(',')
# c = float(dd[0]) + int(dd[1])
# print(c)

print()

print('(1)산술연산자')
a = "My name"
b = "is None"
print(a + ' ' + b)
c = 'I\'ll be '
d = 100
# print(c + d)  # 문자열과 숫자의 덧셈은 불가
print(c + str(d))

print('안녕' * 5 * 5)
# print('ddd' / 3)  # 문자열은 나눗셈 불가능
# print(10 / 0)  # 0으로 나눗셈 불가

print("10 // 3 =", 10 // 3)
print("10 % 3 =", 10 % 3)
print("5 ** 1.5 =", 5 ** 1.5)

print()
print('(2)관계연산자')
a = 30
b = 20
c = a > b
print(c)
print(type(a), type(c))

d = True
print(type(d))

print("10 == 20 :", 10 == 20)
print("10 != 20 :", 10 != 20)

# Next Day 예고
print("10 == 20 or 10 != 20 :", 10 == 20 or 10 != 20)   # Java : ||




