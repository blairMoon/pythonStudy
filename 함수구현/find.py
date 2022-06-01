
nums = [1, 3, 4, 2, 7]
find_number = int(input())

def find_fuc(nums, find_number):
    index = -1
    for i in nums:
        index += 1
        if find_number == i:
            break 
    if find_number not in nums:
        index = -1        
    
    return index 

print(find_fuc(nums, find_number))

 

'''
string = "Hello World"
index = -1
while True:
	index = string.find("o", index+1)    
	if index == -1:        
		break    
	print(index)

'''