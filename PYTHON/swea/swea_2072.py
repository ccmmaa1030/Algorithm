import sys
sys.stdin = open("PYTHON/swea/2072_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    sum = 0
    for i in N:
        if i % 2 == 1:
            sum += i
    print(f'#{test_case} {sum}')