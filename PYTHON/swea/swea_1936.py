import sys
sys.stdin = open("PYTHON/swea/1936_input.txt", "r")

A, B = map(int, input().split())
if A-B == -1 or A-B == -2 or A-B == 2:
    print('B')
elif A-B == 1 or A-B == 2:
    print('A')
