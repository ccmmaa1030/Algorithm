import sys
sys.stdin = open("PYTHON/swea/2029_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    a, b = map(int, input().split())
    print(f'#{test_case} {a//b} {a%b}')
