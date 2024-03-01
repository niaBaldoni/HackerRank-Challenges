from collections import OrderedDict

n = int(input())

ord_dict = OrderedDict()

for i in range(n):
    item_name, space, net_price = input().rpartition(" ")
    # ord_dict[item_name] = ord_dict.get(item_name, 0) + int(net_price)
    if item_name not in ord_dict:
        ord_dict[item_name] = int(net_price)
    else:
        ord_dict[item_name] += int(net_price)

for key, value in ord_dict.items():
    print(key, value)
