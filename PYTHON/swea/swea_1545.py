import sys

sys.stdin = open("PYTHON/swea/1545_input.txt", "r")

N = int(input())  # 주어진 숫자 N

for n in range(N, -1, -1):  # N부터 0까지 1씩 줄어들면서 거꾸로
    print(n, end=" ")  # 해당 숫자를 출력
