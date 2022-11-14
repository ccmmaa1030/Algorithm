import sys

sys.stdin = open("PYTHON/swea/2072_input.txt", "r")

T = int(input())  # 테스트케이스 개수 T

for t in range(1, T + 1):
    N_list = list(map(int, input().split()))  # 주어진 숫자 리스트
    answer = 0  # 합계를 구할 변수

    for n in N_list:
        if n % 2 == 1:  # 홀수이면(2로 나누었을 때 나머지 1)
            answer += n  # 해당 숫자 더하기

    print(f"#{t} {answer}")
