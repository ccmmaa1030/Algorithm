import sys

sys.stdin = open("PYTHON/swea/2047_input.txt", "r")

word = input()  # 입력받은 문장

for c in word:  # 각 문자가
    if ord(c) >= 97:  # 소문자이면(아스키코드 97 이상)
        print(chr(ord(c) - 32), end="")  # 대문자로 변환 후 출력, ""(공백)으로 연결
    else:  # 대문자이면
        print(c, end="")  # 출력, ""(공백)으로 연결
