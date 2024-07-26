from itertools import product

K, M = map(int, input().split())
lists = []

for _ in range(K):
    lst = list(map(int, input().split()))[1:] 
    lists.append(lst)


max_value = 0
for combination in product(*lists):
    current_value = sum(x**2 for x in combination) % M
    max_value = max(max_value, current_value)

print(max_value)
