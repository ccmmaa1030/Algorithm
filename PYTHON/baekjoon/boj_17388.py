S, K, H = map(int, input().split()) # 숭실대, 고려대, 한양대 참여도

if S + K + H >= 100:                # 참여도의 합이 100 이상이면
    print('OK')                     # OK
else:                               # 100 미만이면
    if S == min(S, K, H):           # 참여도가 최솟값과 같은 같으면
        print('Soongsil')           # 해당 학교 이름 출력
    elif K == min(S, K, H):
        print('Korea')
    elif H == min(S, K, H):
        print('Hanyang')