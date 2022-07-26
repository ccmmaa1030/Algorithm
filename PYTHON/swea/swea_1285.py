import sys
sys.stdin = open("PYTHON/swea/1285_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    stone = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if stone[i] < 0:
            stone[i] = stone[i]*(-1)
    stone.sort()
    for i in range(N):
        if stone[i] == stone[0]:
            cnt += 1
    print(f'#{test_case} {stone[0]} {cnt}')
