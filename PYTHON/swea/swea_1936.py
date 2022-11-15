import sys

sys.stdin = open("PYTHON/swea/1936_input.txt", "r")

A, B = map(int, input().split())  # 주어진 두 숫자 a, b

if A - B == -2 or A - B == 1:  # A가 이길 경우 : A - B의 값이 -2 또는 1
    print("A")
else:  # B가 이길 경우 : A - B의 값이 -1 또는 2
    print("B")

# 가위:1, 바위:2, 보:3
# A가 이길 경우 : (가위-보, -2), (바위-가위, 1), (보-바위, 1)
# B가 이길 경우 : (가위-바위, -1), (바위-보, -1), (보-가위, 2)
