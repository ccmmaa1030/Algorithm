import sys
sys.stdin = open("PYTHON/swea/2058_input.txt", "r")

N = int(input())
result = 0

while True:
    result += N % 10
    N = N // 10
    if N == 0:
        break

print(result)