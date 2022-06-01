
nums = [1, 3, 4, 2, 7]
find_number = int(input())

def find(nums, find_number):
    index = 0
    for i in nums:
        if find_number == i:
            index += 1
            break 
        return index
print(find(nums, find_number))

 

'''
string = "Hello World"
index = -1
while True:
	index = string.find("o", index+1)    
	if index == -1:        
		break    
	print(index)

'''