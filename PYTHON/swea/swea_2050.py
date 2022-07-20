import sys
sys.stdin = open("PYTHON/swea/2050_input.txt", "r")

C = {}
C = input()

for i in range(0, len(C)):
    print(ord(C[i])-64, end=' ')
    i += 1

