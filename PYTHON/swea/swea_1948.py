import sys

sys.stdin = open("PYTHON/swea/1948_input.txt", "r")

T = int(input())  # 테스트케이스 T

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 달 별 일수

for test_case in range(1, T + 1):
    answer = 0  # 날짜 차이
    m1, d1, m2, d2 = map(int, input().split())  # 날짜 2개

    if m1 == m2:  # 같은 달이면
        answer = d2 - d1 + 1  # 뒤 - 앞 + 1
    else:  # 다른 달이면
        answer = day[m1 - 1] - d1 + 1 + d2  # 앞의 달 일수차 + 뒤의 달 일수
        for m in range(m1, m2 - 1):  # 중간 달 일수 계산
            answer += day[m]  # 중간 일수 더하기

    print(f"#{test_case} {answer}")
