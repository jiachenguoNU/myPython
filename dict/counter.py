import collections
counter = collections.Counter()
counter[1] += 1; counter['a'] += 1; counter[3.14] += 1
print(type(counter))
for key, value in counter.items():
    print(f"{key}: {value}")