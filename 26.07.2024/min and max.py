import numpy as np

n, m = map(int, input().split())  
my_array = np.array([input().split() for _ in range(n)], int)

min_values = np.min(my_array, axis=1)

max_of_min = np.max(min_values)

print(max_of_min)
