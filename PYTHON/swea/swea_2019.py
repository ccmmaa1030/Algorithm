import sys

sys.stdin = open("PYTHON/swea/2019_input.txt", "r")

N = int(input())  # 주어진 횟수

for n in range(N + 1):
    print(2**n, end=" ")  # 2의 0~N제곱 출력
