import sys

sys.stdin = open("PYTHON/swea/1940_input.txt", "r")

T = int(input())  # 테스트케이스 T

for test_case in range(1, T + 1):
    N = int(input())  # N개 커맨드 실행
    V = 0  # 속도 V
    D = 0  # 거리 D

    for n in range(N):
        c = list(map(int, input().split()))  # 현재 커맨드 리스트(초, 속도)
        if c[0] == 1:  # 가속
            V += c[1]  # 속도만큼 거리 증가
        elif c[0] == 2:  # 감속
            V -= c[1]  # 속도만큼 거리 감소
            if V < 0:  # 현재 속도보다 감속 속도가 크면
                V = 0  # 멈추기 때문에 거리 이동 없음
        D += V

    print(f"#{test_case} {D}")
