from collections import OrderedDict
items = OrderedDict()
n = int(input().strip())
for _ in range(n):
    data = input().split()
    price = int(data[-1])
    item_name = " ".join(data[:-1])
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price
for item_name, net_price in items.items():
    print(item_name, net_price)
