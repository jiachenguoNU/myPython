def explicit_return_none():
    print("This function explicitly returns None.")
    return  # Just like your image

def implicit_return_none():
    print("This function implicitly returns None.")
    # No return statement at all

# --- Let's see the output ---

result_a = explicit_return_none()
print(f"Result from explicit_return_none: {result_a}")
print(f"Type of result_a: {type(result_a)}")

print("---")

result_b = implicit_return_none()
print(f"Result from implicit_return_none: {result_b}")
print(f"Type of result_b: {type(result_b)}")