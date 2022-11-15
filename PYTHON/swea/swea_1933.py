import sys

sys.stdin = open("PYTHON/swea/1933_input.txt", "r")

N = int(input())  # 주어진 숫자 N

for n in range(1, N + 1):  # 1부터 N까지
    if N % n == 0:  # N을 해당 숫자로 나눴을 때 나머지가 0이면 약수
        print(n, end=" ")
