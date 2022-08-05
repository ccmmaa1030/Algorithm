import sys
sys.stdin = open("PYTHON/swea/2001_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr_N = []
    for i in range(N):
        arr_N.append(list(map(int, input().split())))

    fly_kill = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for mi in range(M):
                for mj in range(M):
                    if i+mi < N and j+mj < N:
                        kill += arr_N[i+mi][j+mj]
            fly_kill.append(kill)

    print(f'#{test_case} {max(fly_kill)}')