import sys
sys.stdin = open("PYTHON/swea/1966_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
    print(f'#{test_case}', end=' ')
    for i in range(N):
        print(num[i], end=' ')
    print()