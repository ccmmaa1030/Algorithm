import sys

sys.stdin = open("PYTHON/swea/2025_input.txt", "r")

N = int(input())  # 주어진 숫자
answer = 0  # 합계를 구할 변수

for i in range(1, N + 1):  # 1부터 N까지
    answer += i  # 더하기

print(answer)
