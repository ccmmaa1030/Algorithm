import sys
sys.stdin = open("PYTHON/swea/1979_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    
    garo = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:
                    garo += 1
                if puzzle[i][j] == 0:
                    cnt = 0

    sero = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or i == N-1:
                if cnt == K:
                    sero += 1
                if puzzle[i][j] == 0:
                    cnt = 0

    print(f'#{test_case} {garo + sero}')