import sys

sys.stdin = open("PYTHON/swea/2071_input.txt", "r")

T = int(input())  # 테스트케이스 개수 T

for t in range(1, T + 1):
    N_list = list(map(int, input().split()))  # 입력받은 10개의 숫자 리스트
    N_sum = sum(N_list)  # 숫자 리스트 합계
    N_avg = int(round((N_sum / 10), 0))  # 10으로 나눈 후, 소수점 첫번째 자리에서 반올림

    print(f"#{t} {N_avg}")
