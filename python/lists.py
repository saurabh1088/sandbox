# --- List example one ---
list_example_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reference_list_example_one = list_example_one

print("List referece example show that both variables point to the same list in memory")
print("list_example_one: ", list_example_one)
print("reference_list_example_one: ", reference_list_example_one)
print("Changing list_example_one will also change reference_list_example_one")
list_example_one.append("new element") # This also shows mixed data types in a list
print("list_example_one: ", list_example_one)
print("reference_list_example_one: ", reference_list_example_one)

# --- List example two ---
list_example_two = [x*2 for x in range(10)]
print("\nList comprehension example to create a list of even numbers from 0 to 18")
print("list_example_two: ", list_example_two)

list_example_three = [x for x in range(100) if x % 2 == 0]
print("\nList comprehension example to create a list of even numbers from 0 to 99")
print("list_example_three: ", list_example_three)

sample_data = ["apple", "bat", "car", "elephant", "dog"]
list_example_four = [x for x in sample_data if len(x) > 4]
print("\nList comprehension example to filter words longer than 4 characters")
print("list_example_four: ", list_example_four)

list_example_five = [x.upper() for x in sample_data]
print("\nList comprehension example to convert all words to uppercase")
print("list_example_five: ", list_example_five)


sample_long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_example_six = ["Even" if x % 2 == 0 else "Odd" for x in sample_long_list]
print("\nList comprehension example to label numbers as 'Even' or 'Odd'")
print("list_example_six: ", list_example_six)

