import sys

sys.stdin = open("PYTHON/swea/2043_input.txt", "r")

P, K = map(int, input().split())  # 비밀번호 P, 주어진 번호 K
cnt = P - K + 1  # K부터 1씩 증가하면서 P를 찾는 횟수

print(cnt)
