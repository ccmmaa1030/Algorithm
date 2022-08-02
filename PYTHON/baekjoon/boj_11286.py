import heapq
import sys
input = sys.stdin.readline

N = int(input())
num = []

for i in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(num, (x, x))
    elif x < 0:
        heapq.heappush(num, (-x, x))
    else:
        if not num:
            print(0)
        else:
            n, m = heapq.heappop(num)
            print(m)