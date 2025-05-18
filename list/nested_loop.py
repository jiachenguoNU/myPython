letters = ['a', 'b', 'c']
nums = [1, 2, 3]

my_list = []
for i in letters:
    for j in nums:
        my_list.append((i, j))
print(my_list)


my_list = [(i, j) for i in letters for j in nums]
print(my_list)