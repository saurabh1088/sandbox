import time

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, element in enumerate(array):
    print(f"Index: {index}, Address: {id(element)}, Value: {element}")
    
array_cost_of_insertion = list(range(100))
print(array_cost_of_insertion)

# Insert at end (fast)
start = time.time()
array_cost_of_insertion.append(420)
print("After append:", array_cost_of_insertion)
print("Time taken (append):", time.time() - start)

# Insert at beginning (slow)
start = time.time()
array_cost_of_insertion.insert(0, 0)
print("After insert at start:", array_cost_of_insertion)
print("Time taken (insert at start):", time.time() - start)
