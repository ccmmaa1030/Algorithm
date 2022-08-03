a, b = input().split()

look_good = int(a) + int(b)
look_5 = int(a.replace('6', '5')) + int(b.replace('6', '5'))
look_6 = int(a.replace('5', '6')) + int(b.replace('5', '6'))

max = max(look_good, look_5, look_6)
min = min(look_good, look_5, look_6)

print(min, max)