import sys
sys.stdin = open("PYTHON/swea/2019_input.txt", "r")

T = int(input())

for test_case in range(1, T+2):
    print(1*(2**(test_case-1)), end=' ')