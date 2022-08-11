X = int(input())                        # 영수증에 적힌 총 금액
N = int(input())                        # 구매한 물건 종류
cost = 0                                # 총 금액 계산

for i in range(N):                      # N개의 물건 종류
    a, b = map(int, input().split())    # 각 물건의 가격, 개수
    cost += a * b                       # 총 금액에 추가

if X == cost:                           # 영수증과 계산한 총 금액이 일치하면
    print('Yes')                        # Yes 출력
else:                                   # 일치하지 않으면
    print('No')                         # No 출력