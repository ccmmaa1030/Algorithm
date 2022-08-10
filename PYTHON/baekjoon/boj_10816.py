import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
search = list(map(int, input().split()))

for num in search:
    print(card.count(num), end=' ')