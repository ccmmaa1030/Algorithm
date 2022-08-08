T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    N_M = [str(num) for num in range(N, M+1)]
    cnt = 0

    for i in N_M:
        cnt += i.count('0')
    
    print(cnt)