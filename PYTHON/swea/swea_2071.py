import sys
sys.stdin = open("PYTHON/swea/2071_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    number = map(int, input().split())
    print(f'#{test_case} {int(round((sum(number)/10),0))}')