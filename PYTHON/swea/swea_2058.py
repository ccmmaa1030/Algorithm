import sys

sys.stdin = open("2058_input.txt", "r")

N = input()  # 입력받은 숫자(문자형)
answer = 0  # 합계를 구할 변수

for n in N:  # 각 자릿수
    answer += int(n)  # 정수형으로 변환해서 더하기

print(answer)
