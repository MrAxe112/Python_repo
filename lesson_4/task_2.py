example_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([el for number, el in enumerate(example_list) if example_list[number - 1] < example_list[number]])
