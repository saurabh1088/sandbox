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
