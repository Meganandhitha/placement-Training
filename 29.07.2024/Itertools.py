from itertools import combinations_with_replacement
input_string, r = input().split()
r = int(r)
combinations = combinations_with_replacement(sorted(input_string), r)
for combo in combinations:
    print(''.join(combo)
