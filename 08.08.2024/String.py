def is_pal(s):
    return s == s[::-1]
s = str(input("Enter a string : "))
ans = is_pal(s)
if ans:
    print("Yes")
else:
    print("No")
