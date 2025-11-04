def make_counter():
    count = 0  # 🏠 This variable is "closed over"

    def counter():
        nonlocal count  # 🔑 Gives 'counter' write access to 'count' # if this line is commened out, the next line has to be commented out
        count += 1
        return count

    return counter  # 'counter' is the closure

# --- Usage ---
c1 = make_counter()  # c1 has its own 'count' (starts at 0)
print(c1())  # Output: 1
print(c1())  # Output: 2
print(c1())  # Output: 3

# c2 is a *different* closure with its own *separate* 'count'
c2 = make_counter()
print(c2())  # Output: 1