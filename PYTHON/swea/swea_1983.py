import sys
sys.stdin = open("PYTHON/swea/1983_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    score = []
    for i in range(N):
        mid, end, project = map(int, input().split())
        score.append((mid * 0.35) + (end * 0.45) + (project * 0.2))    
    sort_score = sorted(score, reverse=True)

    grade_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade = ''
    for j in sort_score:
        if j == score[K-1]:
            grade = grade_list[sort_score.index(j) // (N // 10)]

    print(f'#{test_case} {grade}')