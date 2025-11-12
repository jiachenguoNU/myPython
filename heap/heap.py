import heapq

# --- 1. Build the max-heap (your code) ---
original_data = [1, 8, 3, 10, 5]
arr = [-x for x in original_data]
heapq.heapify(arr)

print(f"Initial (negated) max-heap: {arr}")

# --- 2. Get the largest element (Peek) ---
# The root arr[0] is -10. Negating it gives 10.
max_val = -arr[0]
print(f"Largest element is: {max_val}")  # Output: 10

# --- 3. Push a new element ---
new_val = 9
print(f"Pushing {new_val}...")
heapq.heappush(arr, -new_val)
# arr is now [-10, -9, -3, -1, -5, -8]
print(f"Heap after push: {arr}")

# --- 4. Pop the largest element ---
# heappop(arr) returns -10. Negating it gives 10.
popped_max = -heapq.heappop(arr)
print(f"Popped element: {popped_max}")  # Output: 10

# --- 5. See the new largest element ---
# The new root arr[0] is -9. Negating it gives 9.
next_max = -arr[0]
print(f"New largest element is: {next_max}")  # Output: 9
print(f"Final heap: {arr}")

next_max = -arr[1]
print(f"New largest element is: {next_max}") 
