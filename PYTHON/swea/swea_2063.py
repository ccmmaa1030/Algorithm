import sys
sys.stdin = open("PYTHON/swea/2063_input.txt", "r")

N = int(input())

L = list(map(int, input().split()))
L.sort()

middle = N//2
print(L[middle])
