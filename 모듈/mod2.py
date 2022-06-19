def add(a, b):
    return a + b

def sub(a, b):
    return a - b

PI = 3.121592

class Math:
    def solv(self, r):
        return PI * (r ** 2) # **는 거듭제곱이다 






#if __name__=="__main__":의 의미
# 만약 불러오려는 파일에 print가 있다면 다른 파일에서 이 모듈을 불러올 때 함수가 사용되지 않고 print 값만 출력됨
# 따라서 불러오려는 파일에 if __name__=="__main__": 를 실행하여 본 파일에서는 참이 되어 print되고 다른 모듈에서는
# 거짓이 되어 if문 다음문장이 수행되지 않도록 하기 위함 
if __name__=="__main__":
    print(add(3,4))
    print(sub(4,2))



    
        
