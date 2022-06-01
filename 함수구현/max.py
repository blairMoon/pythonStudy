
num = [5,2,3,4,8]

def max_number(num):
    max = float('-inf')
    for i in num:
        if i >= max:
            max = i 
    return max    

print(max_number(num))        