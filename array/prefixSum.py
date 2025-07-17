nums = [1, 2, 3, 4, 5]

prefix = [nums[0]]

for i in range(len(nums) - 1):
	i += 1
	prefix.append(nums[i] + prefix[i - 1])
	
print(prefix)