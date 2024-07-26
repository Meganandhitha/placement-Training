from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
product_result = product(A, B)
print(" ".join(map(str, product_result)))
