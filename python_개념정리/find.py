
nums = [1,2,3,4,5]
find_number = input()

def find(nums, find_number):
    index = -1 
    for i in nums:
        if find_number in nums:
           index += 1 
           
    return index     

print(find(nums, find_number))      


            
    

#ctrl + x  오려두기   