
'''
#09 9개의 서로 다른 자연수가 있는 리스트를 정의하고,
 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오. 
 예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61 가 리스트에 들어 있으면, 
 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
 '''
 #01
nums = [3, 29, 38, 12, 57, 74, 40, 85, 61]
nums.sort()
print(nums[-1])
print(nums.index(nums[-1]))

#02
nums = [3, 29, 38, 12, 57, 74, 40, 85, 61]
max_number = float('-inf')
for n in nums: 
    if n >= max_number:
        max_number = n
print(max_number)

for n in nums:
    if n == max_number:
        print() 

#03 
max_number = float('-inf')
max_idx = 0

for i in range(len(nums)):
    if max_number <= nums[i]:
        max_number = nums[i]
        max_idx = i 
print(max_idx, max_number)      



