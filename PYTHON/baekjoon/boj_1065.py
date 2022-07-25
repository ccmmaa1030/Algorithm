N = input()
cnt = 0

for i in range(1, int(N)+1):
    if i < 10:
        cnt += 1
    elif i < 100:
        cnt += 1
    elif i < 1000:
        X = list(map(int, str(i)))
        if X[0] - X[1] == X[1] - X[2]:
            cnt += 1

print(cnt) 