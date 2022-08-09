n = int(input())                        # 좌표 개수
Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0    # 각 사분면, 축의 점 개수

for point in range(n):                  # n개의 좌표
    x, y = map(int, input().split())    # 좌표 입력받아 아래 조건 확인
    if x > 0 and y > 0:
        Q1 += 1                         # 1사분면 개수 1 증가
    elif x < 0 and y > 0:
        Q2 += 1                         # 2사분면 개수 1 증가
    elif x < 0 and y < 0:
        Q3 += 1                         # 3사분면 개수 1 증가
    elif x > 0 and y < 0:
        Q4 += 1                         # 4사분면 개수 1 증가
    else:
        AXIS += 1                       # 축 개수 1 증가

print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')                  # f-string으로 형식 지정해서 출력