array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, element in enumerate(array):
    print(f"Index: {index}, Address: {id(element)}, Value: {element}")
