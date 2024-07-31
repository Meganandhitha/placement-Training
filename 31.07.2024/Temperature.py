def n(p):
    if p >= 100.4:
        return "You have a fever."
    else:
        return "You do not have a fever."
np = float(input("Enter your temperature in Fahrenheit: "))
print(n(np))
