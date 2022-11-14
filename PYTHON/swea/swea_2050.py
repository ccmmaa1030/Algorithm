import sys

sys.stdin = open("2050_input.txt", "r")

C = input()  # 입력받은 문자열

for i in C:
    print(ord(i) - 64, end=" ")  # 아스키코드 숫자값에서 64만큼 빼고 출력
