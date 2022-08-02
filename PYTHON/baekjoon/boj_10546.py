import sys
input = sys.stdin.readline

N = int(input())
marathon = dict()
goal = dict()

for i in range(N):
    name = input().rstrip()
    if name in marathon:
        marathon[name] += 1
    else:
        marathon[name] = 1

for i in range(N-1):
    name = input().rstrip()
    if name in goal:
        goal[name] += 1
    else:
        goal[name] = 1

for i in marathon.keys():
    if i not in goal:
        print(i)
        break
    else:
        if marathon[i] != goal[i]:
            print(i)
            break