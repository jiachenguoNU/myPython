letters = ['a', 'b', 'c']
nums = [1, 2, 3]

my_dict = {}
for i, j in zip(letters, nums):  # zip() is used to extract elements from two lists simultaneously
    my_dict[i] = j
print(my_dict)


my_dict = {i: j for i, j in zip(letters, nums)}
print(my_dict)