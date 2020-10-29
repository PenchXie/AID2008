import itertools

# result_list = list(itertools.product(range(1, 7), range(1, 7), range(1, 7)))
result_list = list(itertools.product(range(1, 7), repeat=3))
print(len(result_list))