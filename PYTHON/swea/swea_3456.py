import sys
sys.stdin = open("PYTHON/swea/3456_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    length = list(map(int, input().split()))
    length.sort()

    if length[0] == length[1]:
        answer = length[2]
    else:
        answer = length[0]
    
    print(f'#{test_case} {answer}')