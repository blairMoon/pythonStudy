

sorted_list = list((map(int , input().split())))   


for i in sorted_list: 
    for j in (range(int(len(sorted_list)) - 1)):
        if sorted_list[j] > sorted_list[j + 1]:
            sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
print(sorted_list)           




    