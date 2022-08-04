nemo = []
for i in range(4):
    a, b, c, d = map(int, input().split())
    for length in range(a, c):
        for height in range(b, d):
            nemo.append((length, height))

area = set(nemo)

print(len(area))
