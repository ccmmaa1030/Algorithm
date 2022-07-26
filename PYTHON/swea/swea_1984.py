import sys
sys.stdin = open("PYTHON/swea/1984_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().split()))
    num.sort()
    del num[9]
    del num[0]
    avg = sum(num)/len(num)
    print(f'#{test_case} {round(avg)}')