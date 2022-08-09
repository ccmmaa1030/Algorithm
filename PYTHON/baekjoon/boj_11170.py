T = int(input())

for test_case in range(T):                      # 테스트케이스 개수
    N, M = map(int, input().split())            # 숫자 N, M
    N_M = [str(num) for num in range(N, M+1)]   # N부터 M까지의 숫자를 문자열로 저장
    cnt = 0                                     # 0 카운트

    for i in N_M:                               # N ~ M
        cnt += i.count('0')                     # 해당 숫자의 0을 카운트해서 더함
    
    print(cnt)                                  # 최종 0의 개수 출력