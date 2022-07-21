import sys
sys.stdin = open("PYTHON/swea/1976_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    H = h1 + h2
    M = m1 + m2

    if H > 12:
        H -= 12
    if M > 59:
        M -= 60
        H += 1 

    print(f'#{test_case} {H} {M}')