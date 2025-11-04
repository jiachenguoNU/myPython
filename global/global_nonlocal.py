x = 0  # <-- Let's define a GLOBAL x

def outer_function():
    x = 10  # 🏠 Enclosing variable (This one will be ignored by inner_function)

    def inner_function():
        global x  # 🌍 Tells Python to modify the GLOBAL 'x'
        x = 50

    print(f"Outer (before inner): {x}")  # Prints outer_function's local x
    inner_function()
    print(f"Outer (after inner): {x}")   # Still prints outer_function's local x

print(f"Global (before outer): {x}")
outer_function()
print(f"Global (after outer): {x}")

print("------------------------")
def outer_function():
    x = 10  # 🏠 Enclosing variable (not global)

    def inner_function():
        nonlocal x  # Tells Python to modify the 'x' from 'outer_function'
        x = 50

    print(f"Outer (before inner): {x}")  # Output: Outer (before inner): 10
    inner_function()
    print(f"Outer (after inner): {x}")   # Output: Outer (after inner): 50

outer_function()


print("-----------------------")
x = 0  # 🌍 Global variable

def modify_global():
    global x  # Tells Python to modify the GLOBAL 'x'
    x = 100

print(f"Before: {x}")  # Output: Before: 0
modify_global()
print(f"After: {x}")   # Output: After: 100