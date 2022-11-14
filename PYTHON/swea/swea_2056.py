import sys

sys.stdin = open("2056_input.txt", "r")

T = int(input())  # 테스트케이스 개수 T, 달의 해당하는 날짜 값
DATE = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

for t in range(1, T + 1):
    date = input()  # 입력받은 날짜
    y = date[0:4]  # 문자열 슬라이싱 년 4글자
    m = date[4:6]  # 문자열 슬라이싱 월 2글자
    d = date[6:8]  # 문자열 슬라이싱 일 2글자

    if 0 < int(m) <= 12 and 0 < int(d) <= DATE[int(m)]:  # 1~12월이고, 1~해당하는 날짜까지에 해당하면
        print(f"#{t} {y}/{m}/{d}")  # YYYY/MM/DD 형식으로 출력
    else:  # 유효한 날짜가 아니면
        print(f"#{t} -1")  # -1 출력
