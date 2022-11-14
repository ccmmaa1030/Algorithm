import sys

sys.stdin = open("PYTHON/swea/2068_input.txt", "r")

T = int(input())  # 테스트케이스 개수 T

for t in range(1, T + 1):
    N_list = list(map(int, input().split()))  # 입력받은 숫자 리스트
    answer = max(N_list)  # 리스트에서 최댓값 구하기

    print(f"#{t} {answer}")
