import sys
sys.stdin = open("PYTHON/swea/2005_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}')
    size = int(input())
    num = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(i+1):
            if j == 0 or j == i:
                num[i][j] = 1
            else:
                num[i][j] = num[i][j-1] + num[i-1][j]
            print(num[i][j], end=' ')
        print()