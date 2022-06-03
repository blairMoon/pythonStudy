
nums = [1, 3, 4, 2, 7]
find_number = int(input())

def find_fuc(nums, find_number):
    index = -1
    for i in nums:
        index += 1
        if find_number == i:
            return i 
    return -1 
        

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