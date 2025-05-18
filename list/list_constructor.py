nums = [0,1,2,3,4,5]

my_list = []
for i in nums:
    if i % 2 == 0:
        my_list.append(i**2)
print(my_list)


my_list = [i**2 for i in nums if i % 2 == 0 ]  #if must be at the end
print(my_list)


my_list = [i**3 if i % 2 == 0 else i**4 for i in nums]  #if else not in the end
print(my_list)  