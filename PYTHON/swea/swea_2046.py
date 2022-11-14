import sys

sys.stdin = open("PYTHON/swea/2046_input.txt", "r")

T = int(input())  # 반복 횟수 #

for i in range(1, T + 1):
    print("#", end="")  # 출력 후 ""(공백)으로 연결
