import sys

sys.stdin = open("PYTHON/swea/1948_input.txt", "r")

T = int(input())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T + 1):
    answer = 0
    m1, d1, m2, d2 = map(int, input().split())

    if m1 == m2:
        answer = d2 - d1 + 1
    else:
        answer = day[m1 - 1] - d1 + 1 + d2
        for m in range(m1, m2 - 1):
            answer += day[m]

    print(f"#{test_case} {answer}")
