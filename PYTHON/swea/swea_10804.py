import sys
sys.stdin = open("PYTHON/swea/10804_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    bdpq = input()
    re_bdpq = bdpq[::-1]
    mirror = ''

    for i in re_bdpq:
        if i == 'b':
            mirror += 'd'
        elif i == 'd':
            mirror += 'b'
        elif i == 'p':
            mirror += 'q'
        else:
            mirror += 'p'
    
    print(f'#{test_case} {mirror}')
