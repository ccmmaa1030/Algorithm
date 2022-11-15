import sys

sys.stdin = open("PYTHON/swea/2027_input.txt", "r")

for i in range(5):  # 5행
    for j in range(5):  # 5열
        if i == j:  # 행과 열이 같으면
            print("#", end="")  # # 출력
        else:  # 다르면
            print("+", end="")  # + 출력
    print()  # 개행
