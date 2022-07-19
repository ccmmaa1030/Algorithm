import sys
sys.stdin = open("PYTHON/swea/2043_input.txt", "r")

P, K = map(int, input().split())
cnt = 0

for i in range(K, P+1):
    cnt += 1
    if i == P:
        break

print(cnt)