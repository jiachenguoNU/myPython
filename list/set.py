l = [1, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9]

my_set = set()
for i in l:
    my_set.add(i)
print(my_set)
my_set = {i for i in l}