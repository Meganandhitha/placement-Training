def rev_num_while_loop(num):
    rev_no = 0
    while num > 0:
        last_digit = num % 10
        rev_no = (rev_no * 10) + last_digit
        num = num // 10
    return rev_no 
num = int(input("Input a number to reverse: "))
result = rev_num_while_loop(num)
print("The number after the reverse operation:", result)
