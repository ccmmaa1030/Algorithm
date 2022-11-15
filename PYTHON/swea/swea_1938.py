import sys

sys.stdin = open("PYTHON/swea/1938_input.txt", "r")

a, b = map(int, input().split())  # 주어진 두 숫자 a, b

print(a + b)  # 더하기
print(a - b)  # 빼기
print(a * b)  # 곱하기
print(a // b)  # 나누기
