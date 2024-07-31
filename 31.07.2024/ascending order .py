def ss(a, b, c):
    return sorted([a, b, c])
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
s = ss(num1, num2, num3)
print(f"The numbers in ascending order are: {s}")
