N, M = map(int,input().split())
castle = []

for i in range(N):
    castle.append(list(input()))

N_guard = 0
M_guard = 0

for n in range(N):
    if "X" not in castle[n]:
        N_guard += 1

for m in range(M):
    if "X" not in [castle[n][m] for n in range(N)]:
        M_guard += 1

print(max(N_guard ,M_guard))