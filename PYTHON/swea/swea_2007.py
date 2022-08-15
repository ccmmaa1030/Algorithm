import sys
sys.stdin = open("PYTHON/swea/2007_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    string = input().strip()

    for i in range(11):
        code = string[:i]
        next = string[i:i*2]

        if i != 0 and code == next:
            answer = len(code)
            break

    print(f'#{test_case} {answer}')