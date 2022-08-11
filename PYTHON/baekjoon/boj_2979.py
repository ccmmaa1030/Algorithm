A, B, C = map(int, input().split())         # 트럭 수 당 주차요금

time = [0] * 100                            # 시간대(1~100)별 주차된 트럭 수
for i in range(3):
    start, end = map(int, input().split())  # 도착 시간, 떠난 시간
    for i in range(start, end):             # 도착~떠난 시간 동안
        time[i] += 1                        # 해당 시간대에 주차된 트럭 수 1 증가

cost = 0                                    # 주차 요금
for car in time:                            # 시간대별 주차된 트럭 수가
    if car == 1:                            # 1대이면
        cost += A                           # 해당 시간대는 주차 요금이 A
    elif car == 2:                          # 2대이면
        cost += B * 2                       # 해당 시간대는 주차 요금이 B * 2
    elif car == 3:                          # 3대이면
        cost += C * 3                       # 해당 시간대는 주차 요금이 C * 3

print(cost)                                 # 최종 주차 요금 출력


# time 리스트 예시
# 시간대  0  1  2  3  4  5  6  7  8 ... 99
# 1 ~ 6      v  v  v  v  v
# 3 ~ 5            v  v
# 2 ~ 8         v  v  v  v  v  v
# 트럭 수     1  2  3  3  2  1  1
# 요금        A  B  C  C  B  A  A