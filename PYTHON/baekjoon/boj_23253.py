import sys
input = sys.stdin.readline

N, M = map(int, input().split())
possible = "Yes"

for i in range(1, M+1):
    k = int(input())
    ki = list(map(int, input().split()))
    
    for idx in range(k-1):
        if ki[idx] < ki[idx+1]:
            possible = "No"
            break

print(possible)