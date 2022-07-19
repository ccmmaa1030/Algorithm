import sys
sys.stdin = open("PYTHON/swea/1933_input.txt", "r")

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')