angle = [int(input()) for i in range(3)]    # 세 각 입력받아 리스트에 저장
angle_sum = sum(angle)                      # 세 각의 합
cnt = len(set(angle))                       # 중복을 제거한 후 각의 개수

if cnt == 1 and angle_sum == 180:           # 값이 1 종류이고, 합이 180인 경우
    print('Equilateral')                    
elif cnt == 2 and angle_sum == 180:         # 값이 2 종류이고, 합이 180인 경우
    print('Isosceles')
elif cnt == 3 and angle_sum == 180:         # 값이 3 종류이고, 합이 180인 경우
    print('Scalene')
else:                                       # 합이 180이 아닌 경우
    print('Error')