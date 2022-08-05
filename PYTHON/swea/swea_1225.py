import sys
sys.stdin = open("PYTHON/swea/1225_input.txt", "r")

for test_case in range(10):
    T = int(input())
    code = list(map(int, input().split()))

    while True:
        minus = 1
        for minus in range(1, 6):
            code.append(code.pop(0) - minus)
            if code[-1] <= 0:
                code[-1] = 0
                break
        if code[-1] == 0:
            break
    
    print(f'#{T}', *code)