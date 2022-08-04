N = int(input())

condo = []
for n in range(N):
    condo.append(list(input()))

garo, sero = 0, 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if condo[i][j] == '.' and j < N-1:
            cnt += 1

        elif condo[i][j] == '.' and j == N-1:
            cnt += 1
            if cnt >= 2:
                garo += 1
        
        elif condo[i][j] == 'X':
            if cnt >= 2:
                garo += 1
            cnt = 0

for j in range(N):
    cnt = 0
    for i in range(N):
        if condo[i][j] == '.' and i < N-1:
            cnt += 1

        elif condo[i][j] == '.' and i == N-1:
            cnt += 1
            if cnt >= 2:
                sero += 1

        elif condo[i][j] == 'X':
            if cnt >= 2:
                sero += 1
            cnt = 0

print(garo, sero)