T = int(input())

for testcase in range(1, T+1):
    OX = input()
    score = 0
    point = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            point += 1
            score += point
        else:
            point = 0
    print(score)