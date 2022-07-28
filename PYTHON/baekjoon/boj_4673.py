num = set(range(1, 10001))
d_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    d_num.add(i)

s_num = sorted(num - d_num)

for i in s_num:
    print(i)
