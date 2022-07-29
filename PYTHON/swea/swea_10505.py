import sys
sys.stdin = open("PYTHON/swea/10505_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    
    income_avg = sum(income) / N
    avg_down = 0

    for i in range(N):
        if income[i] <= income_avg:
            avg_down += 1

    print(f'#{test_case} {avg_down}')