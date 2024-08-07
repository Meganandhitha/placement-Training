def string_to_dict(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
input_string = "Github"
result = string_to_dict(input_string)
print(result)
