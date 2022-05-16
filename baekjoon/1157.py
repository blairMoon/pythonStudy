'''
알파벳 대소문자로 된 단어가 주어지면, 

이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 

단, 대문자와 소문자를 구분하지 않는다.

첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 

단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''
word = input()
word = word.upper()    #결국 대문자로 출력해야하니까 대문자로 먼저 다 변환 
word_list = list(set(word))   #for문 돌릴 때 값이 중복되므로 set함수를 써서 중복 제거 (why?)
num = []                    #num이라는 리스트를 만듦
 
for i in word_list:
    num.append(word.count(i))    # num에 for문을 돌리면서 알파벳의 개수를 추가함 
index = num.index(max(num))      # index라는 변수에 num의 최댓값의 위치를 넣어줌 
 
if num.count(max(num)) > 1:      # num의 최댓값의 갯수가 1보다 크면 ? 출력
    print("?")
else:
    print(word_list[index])     # 그게 아니라면 index에 있는 num의 최댓값의 위치의 알파벳을 출력함 


