import sys
sys.stdin = open("PYTHON/swea/2068_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    max = 0
    for i in N:
        if i > max:
            max = i
    print(f'#{test_case} {max}')