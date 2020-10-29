import itertools

pwd_str = "abfghi0123"

[print(item) for item in itertools.permutations(pwd_str, 6)]

count = 0
for item in itertools.combinations(range(5), 3):
    count += 1

print(count)