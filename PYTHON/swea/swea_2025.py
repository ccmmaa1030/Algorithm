import sys
sys.stdin = open("PYTHON/swea/2025_input.txt", "r")

N = int(input())
result = 0

for i in range(1, N+1):
    result += i

print(result)