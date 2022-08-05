import sys
sys.stdin = open("PYTHON/swea/5431_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))

    no_submit = []
    for i in range(1, N+1):
        if i not in submit:
            no_submit.append(i)

    print(f'#{test_case}', *no_submit)