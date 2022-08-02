import sys
input = sys.stdin.readline

N = int(input())

num = []
for i in range(N):
    n = int(input())
    num.append(n)

num.sort()

for i in range(N):
    print(num[i])