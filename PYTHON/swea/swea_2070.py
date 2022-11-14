import sys

sys.stdin = open("PYTHON/swea/2070_input.txt", "r")

T = int(input())  # 테스트케이스 개수 T

for t in range(1, T + 1):
    a, b = map(int, input().split())  # 입력받은 2개의 수

    if a > b:  # a가 더 크면
        print(f"#{t} >")  # > 출력
    elif a < b:  # b가 더 크면
        print(f"#{t} <")  # < 출력
    else:  # 두 수가 같으면
        print(f"#{t} =")  # = 출력
