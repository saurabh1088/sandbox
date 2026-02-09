import copy

# ----------------------------------------------
# Copy and Deepcopy in Python

# Shallow Copy
original_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)

print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)

# Modifying the inner list of the original list
original_list[0][0] = -1
original_list[0][1] = -2
original_list[0][2] = -3
original_list[0][3] = -4

print("\nAfter modifying the original list:")
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)
print("Deep Copied List:", deep_copied_list)

