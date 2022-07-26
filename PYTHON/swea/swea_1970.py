import sys
sys.stdin = open("PYTHON/swea/1970_input.txt", "r")

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cnt = [0, 0, 0, 0, 0, 0, 0, 0]

for test_case in range(1, T+1):
    N = int(input())

    for i in range(len(money)):
        cnt[i] = N // money[i]
        N = N % money[i]
    
    print(f'#{test_case}')
    for j in range(len(cnt)):
        print(cnt[j], end=' ')
    print()
