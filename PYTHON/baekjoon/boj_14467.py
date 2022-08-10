N = int(input())                            # 관찰 횟수
cow = {}                                    # 소의 번호, 최근 위치
move = {}                                   # 소의 번호, 이동횟수

for n in range(N):                          # N번 관찰
    num, pos = map(int, input().split())    # 소의 번호, 현재 위치

    if num not in cow:                      # cow에 해당 소 번호가 없으면
        cow[num] = pos                      # cow에 위치 저장
        move[num] = 0                       # move에 이동횟수 초기값 0 저장

    else:                                   # cow에 해당 소 번호가 있으면
        if cow[num] != pos:                 # 최근 위치와 현재 위치가 다르면
            cow[num] = pos                  # cow에 위치 갱신
            move[num] += 1                  # move에 해당 소 번호의 이동횟수 +1 
    
print(sum(move.values()))                   # move의 이동횟수 합 출력