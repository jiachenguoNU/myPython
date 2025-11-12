my_list = [10, 20, 30, 40, 50]
# Index:    0   1   2   3   4
# Neg Idx: -5  -4  -3  -2  -1

# --- Single Items ---

# First item (Index 0)
print(f"First:  {my_list[0]}")
# Output: First:  10

# Last item (Index -1)
print(f"Last:   {my_list[-1]}")
# Output: Last:   50

# --- Slicing ---

# Slice from index 1 UP TO (but not including) index 4
# Start = 1 (INCLUDED) -> 20
# Stop  = 4 (EXCLUDED) -> 50
print(f"Slice:  {my_list[1:4]}")
# Output: Slice:  [20, 30, 40]

print(f"Slice:  {my_list[1:-1]}")
# Output: Slice:  [20, 30, 40]

print(f"Slice:  {my_list[1:]}")
# Output: Slice:  [20, 30, 40]