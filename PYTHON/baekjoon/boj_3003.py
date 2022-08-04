chess = [1, 1, 2, 2, 2, 8]
find = list(map(int, input().split()))

for i in range(6):
    if find[i] != chess[i]:
        print(chess[i]-find[i], end=' ')
    else:
        print(0, end=' ')