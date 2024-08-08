n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print('Old value of n1 is {0} and n2 is {1}'.format(n1, n2))
n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print('New value of n1 is {0} and n2 is {1}'.format(n1, n2))
