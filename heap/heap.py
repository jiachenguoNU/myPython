import heapq

def convert_list_to_heap_and_print(input_list):
    """
    Converts a given list into a min-heap in-place and then prints the heap.

    Args:
        input_list: The list to be converted to a heap.
    """
    print(f"Original list: {input_list}")

    # Convert the list to a heap in-place.
    # After this operation, input_list will satisfy the min-heap property.
    heapq.heapify(input_list)

    print(f"List after heapify (now a min-heap): {input_list}")

    # To demonstrate the heap property, let's extract elements.
    # Note: Printing the list directly after heapify will show it as an array
    # that satisfies the heap property, but not necessarily fully sorted.
    # To see the elements in sorted order, you need to extract them one by one.

    # print("\nExtracting elements one by one (will be in sorted order):")
    # extracted_elements = []
    # while input_list:
    #     smallest = heapq.heappop(input_list)
    #     extracted_elements.append(smallest)
    #     print(f"Extracted: {smallest}, Remaining heap: {input_list}")

    # print(f"\nAll elements extracted in sorted order: {extracted_elements}")


# --- Test Cases ---
my_list_1 = [4, 1, 7, 3, 8, 2, 6]
convert_list_to_heap_and_print(my_list_1)

print("\n" + "="*30 + "\n")

my_list_2 = [9, 5, 1, 8, 2]
convert_list_to_heap_and_print(my_list_2)

print("\n" + "="*30 + "\n")

my_list_3 = []
convert_list_to_heap_and_print(my_list_3)

print("\n" + "="*30 + "\n")

my_list_4 = [5]
convert_list_to_heap_and_print(my_list_4)