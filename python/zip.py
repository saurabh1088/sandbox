list_a = ["Batman", "Superman", "Wonder Woman"]
list_b = ["Bruce Wayne", "Clark Kent", "Diana Prince"]

# Using zip to combine the two lists
combined = zip(list_a, list_b)
print(list(combined))

list_c = ["Gotham", "Metropolis", "Themyscira"]
# Using zip to combine three lists
combined_three = zip(list_a, list_b, list_c)
print(list(combined_three))

# uneven lists
list_d = ["Robin", "Supergirl"]
# Using zip with uneven lists
combined_uneven = zip(list_a, list_b, list_d)
print(list(combined_uneven))

list_one = [1, 2, 3]
list_two = [1, 2, 3]

# creating a dictionary using zip
list_keys = ["one", "two", "three"]
list_values = [1, 2, 3]
dictionary_from_zip = dict(zip(list_keys, list_values))
print(dictionary_from_zip)

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
print(add_item("orange"))
# Here the output will be ['apple', 'banana', 'orange'] because the default list is shared across all calls to the function.
# To avoid this, we can use None as the default value and create a new list inside the function if items is None.
