nums = [1,2,3]

def min_max(nums):
    max_num = float('-inf')
    min_num = float('inf')
    for i in nums:
        if i >= max_num:
            max_num = i 
        if i <= min_num:
            min_num = i 
    return max_num, min_num

print(min_max(nums))        


# 전역 변수 (global variable)
# 지역 변수 (local variable)
        
        