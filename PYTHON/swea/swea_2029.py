import sys

sys.stdin = open("PYTHON/swea/2029_input.txt", "r")

T = int(input())  # 테스트케이스 개수 T

for t in range(1, T + 1):
    a, b = map(int, input().split())  # 입력받은 두 수 a, b
    q = a // b  # 몫
    r = a % b  # 나머지
    print(f"#{t} {q} {r}")
