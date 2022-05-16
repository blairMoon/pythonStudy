'''
#08 N개의 정수가 들어 있는 리스트를 정의하고, 최솟값과 최댓값을 출력하는 프로그램을 작성하시오.
'''
'''
#01
nums = [20, 10, 35, 30, 7]
nums.sort()
print(nums[0],nums[4])

#02
print(max(nums))
print(min(nums))
'''
#03 
nums = [20, 10, 35, 30, 7]
max_num = 0 
for n in nums:
    if max_num <= n:
        max_num = n    
print(max_num)
# shift + tab 들여쓰기의 반대          




