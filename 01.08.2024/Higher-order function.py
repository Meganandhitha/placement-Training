def apply_function(func, values):
    return [func(value) for value in values]

print(apply_function(lambda x: x * 2, [1, 2, 3, 4])) 
