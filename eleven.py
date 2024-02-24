melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455,'Si': 1415, 'Be': 1287}
first_el, second_el = map(str, input().split())
difference = melt[first_el] - melt[second_el]
print(difference)