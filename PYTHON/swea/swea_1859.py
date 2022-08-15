import sys
sys.stdin = open("PYTHON/swea/1859_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    max_price = price[-1]
    answer = 0

    for i in range(N-2, -1, -1):
        if price[i] >= max_price:
            max_price = price[i]
        else:
            answer += max_price - price[i]
    
    print(f'#{test_case} {answer}')