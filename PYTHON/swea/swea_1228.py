import sys
sys.stdin = open("PYTHON/swea/1228_input.txt", "r")

T = 10
for test_case in range(1, T+1):
    code_len = int(input())
    code = list(input().split())
    cmd_cnt = int(input())
    cmd = list(input().split())

    x = 0
    y = 0
    s = 0
    for i in range(len(cmd)):
        if cmd[i] == "I":
            x = int(cmd[i+1])
            y = int(cmd[i+2])
            s = i+3
            while True:
                code.insert(x, cmd[s])
                if s == i+2+y:
                    break
                x += 1
                s += 1
    
    print(f'#{test_case}', end=' ')
    for i in range(10):
        print(code[i], end=' ')
    print()